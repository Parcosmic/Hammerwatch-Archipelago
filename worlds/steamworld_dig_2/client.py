# Shamelessly stolen from Cave Story
import asyncio
import json
from typing import Tuple, Dict, Any
from enum import Enum
from pathlib import Path
import subprocess
import sys
import os
import uuid
from .patcher import *
from . import SWD2World
import Utils
from NetUtils import NetworkItem
from .names import const
from .locations import all_locations

from CommonClient import CommonContext, server_loop, gui_enabled, ClientCommandProcessor, logger, \
    get_base_parser

DEFAULT_RCON_PORT = 4353


class SWD2Packet(Enum):
    READINFO = 0

    ERROR = 255
    DISCONNECT = 255


class SWD2ClientCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    # def _cmd_tsc(self, script: str) -> bool:
    #     """Execute the following TSC Comand"""
    #     if self.ctx.cs_streams:
    #         Utils.async_start(send_packet(self.ctx, encode_packet(CSPacket.RUNTSC, script)))
    #         return True
    #     return False
    #
    # def _cmd_cs_sync(self, script: str):
    #     """Force a sync to occur"""
    #     self.ctx.syncing = True


class SWD2Context(CommonContext):
    command_processor = SWD2ClientCommandProcessor
    game = const.game
    items_handling = 0b101

    def __init__(self, args):
        super().__init__(args.connect, args.password)
        self.client_streams: Tuple = None
        self.client_connected = False
        self.patched = asyncio.Event()
        self.game_watcher_task = None
        self.locations = [False] * len(all_locations)
        self.game_dir = os.path.dirname(SWD2World.settings.game_path)
        if args.rcon_port:
            self.rcon_port = args.rcon_port
        else:
            self.rcon_port = DEFAULT_RCON_PORT
        self.syncing = False
        self.want_slot_data = True
        self.slot_data: Dict[str, Any] = None

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(SWD2Context, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            if not self.patched.is_set():
                Utils.async_start(self.send_msgs([
                    {
                        "cmd": "LocationScouts",
                        "locations": self.server_locations,
                        "create_as_hint": 0,
                    }
                ]))
                self.slot_data = args["slot_data"]
            else:
                launch_game(self)
        elif cmd == "LocationInfo":
            if not self.patched.is_set():
                patch_game(self)
                launch_game(self)
        elif cmd == "ReceivedItems":
            if self.patched.is_set():
                self.syncing = True

    def run_gui(self):
        """Import kivy UI system and start running it as self.ui_task."""
        from kvui import GameManager

        class SWD2Manager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago SteamWorld Dig 2 Client"

        self.ui = SWD2Manager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


def encode_packet(pkt_type: SWD2Packet, data=None, addr: int = None):
    if not data:
        return pkt_type.value.to_bytes(1, "little") + (b'\x00'*4)
    # data_bytes = data.encode()
    # return pkt_type.value.to_bytes(1, 'little') + len(data_bytes).to_bytes(4, 'little') + data_bytes


def decode_packet(ctx: SWD2Context, pkt_type: SWD2Packet, data_bytes: bytes, sync: bool = False):
    if pkt_type == SWD2Packet.READINFO:
        data = json.loads(data_bytes.decode())
        # ctx.offsets = data['offsets']
        logger.info(f"Connected to \'{data['platform']}\' client using API v{data['api_version']} with UUID {data['uuid']}")
    return None


async def send_packet(ctx: SWD2Context, pkt: bytes, sync: bool = False):
    reader, writer = ctx.client_streams
    writer.write(pkt)
    await asyncio.wait_for(writer.drain(), timeout=1.5)
    header = await asyncio.wait_for(reader.read(5), timeout=5)
    if header:
        pkt_type = SWD2Packet(header[0])
        length = int.from_bytes(header[1:4], "little")
        if length > 0:
            data_bytes = await asyncio.wait_for(reader.read(length), timeout=5)
            return decode_packet(ctx, pkt_type, data_bytes, sync)
        else:
            data_bytes = None


def teardown(ctx, msg):
    logger.debug(msg)
    ctx.client_streams = None
    ctx.client_connected = False


def patch_game(ctx: SWD2Context):
    logger.info("Patching game")
    locations: Dict[int, NetworkItem] = ctx.locations_info
    patch_files(locations, ctx.game_dir, ctx.slot_data, ctx.items_received)
    ctx.patched.set()


def launch_game(ctx: SWD2Context):
    logger.info("Starting SteamWorld Dig 2")
    exec_dir = Path(ctx.game_dir).expanduser()
    exec_path = Path(exec_dir).joinpath("Dig2.exe")
    subprocess.Popen([exec_path], cwd=exec_dir)
    ctx.syncing = True
    teardown(ctx, "Mod hasn't been implemented yet, disconnecting")


async def swd2_connector(ctx: SWD2Context):
    await ctx.patched.wait()
    logger.info("Starting SteamWorld Dig 2 connector")
    while not ctx.exit_event.is_set():
        try:
            if not ctx.client_connected:
                ctx.client_streams = await asyncio.wait_for(asyncio.open_connection("localhost", ctx.rcon_port), timeout=4)
                if ctx.client_streams:
                    # Read initial info from client
                    # await send_packet(ctx, encode_packet(SWD2Packet.SOMETHINGIDK))
                    pass
                ctx.client_connected = True
                logger.info("Successfully connected to SteamWorld Dig 2")
            elif ctx.client_streams:
                # Poll client for stuff
                pass
        except TimeoutError:
            teardown(ctx, "Connection timed out, attempting to reconnect...")
            continue
        except ConnectionRefusedError:
            teardown(ctx, "Connection refused, attempting to reconnect...")
            continue
        except (ConnectionResetError, ConnectionAbortedError):
            teardown(ctx, "Connection lost, attempting to reconnect...")
            continue


async def main(args):
    ctx = SWD2Context(args)
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()
    ctx.game_watcher_task = asyncio.create_task(swd2_connector(ctx), name="game connector")

    await ctx.exit_event.wait()
    ctx.server_address = None

    await ctx.shutdown()

    if ctx.game_watcher_task:
        await ctx.game_watcher_task


def launch():
    parser = get_base_parser(description="SteamWorld Dig 2 Client, for text interfacing.")
    parser.add_argument('--rcon-port', default=str(DEFAULT_RCON_PORT),
                        type=int, help='Port to use to communicate with SteamWorld Dig 2')
    args, rest = parser.parse_known_args()

    import colorama
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()
