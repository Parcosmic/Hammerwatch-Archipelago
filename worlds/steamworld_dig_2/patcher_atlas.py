import os

from . import patch_files
from .client_util import ClientContextData


AP_ATLAS_NAME = "archipelago-items-ltf_0"

ap_sprites = {
    "Effects/Textures/Pickups/ap_container_core": (190, 0, 34, 36),
    "Sprites/Archipelago/ap_item_1": (0, 0, 96, 96),
    "Sprites/Archipelago/ap_pickup": (98, 0, 90, 90),
}

def patch_atlas_and_sprites(ctx: ClientContextData):
    from importlib.resources import files

    bundle_dir = os.path.join(ctx.game_dir, "Bundle")
    data_dir = os.path.join(bundle_dir, "data01")
    atlases_dir = os.path.join(bundle_dir, "Atlases")

    # Copy AP atlas to the game files
    ap_atlas_png = f"{AP_ATLAS_NAME}.png"
    atlas_bytes = files(patch_files).joinpath(ap_atlas_png).read_bytes()
    with open(os.path.join(atlases_dir, ap_atlas_png), "wb") as atlas_writer:
        atlas_writer.write(atlas_bytes)

    sprite_aliases = {
        "icons-ltf_0": [
            ("Effects/Textures/Pickups/upgrade_container_core", "1043 1918 33 33"),
        ],
    }

    # Init atlases_data with the ap sprites
    atlases_data: dict[str, list[tuple[str, str]]] = {
        AP_ATLAS_NAME: [
            (ap_sprite, f"{rect[0]} {rect[1]} {rect[2]} {rect[3]}") for ap_sprite, rect in ap_sprites.items()
        ],
    }

    # Read atlases map
    with open(os.path.join(atlases_dir, "atlases.map"), "r") as atlases_map_reader:
        current_file = ""
        for line in atlases_map_reader.readlines():
            if line[0] == ':':
                current_file = line[1:-1]  # Trim off the newline
                atlases_data[current_file] = []
                continue
            splits = line.split(" = ")
            atlases_data[current_file].append((splits[0], splits[1][:-1]))

        # Create aliases so we can use any sprite anywhere we want
        for file, aliases in sprite_aliases.items():
            with open(os.path.join(data_dir, "Atlases", f"{file}.txt"), "a") as alias_writer:
                for alias in aliases:
                    atlases_data[file].append(alias)
                    alias_writer.write(f"{alias[0]} = {alias[1]}\r\n")

    # Write the master alias file
    with open(os.path.join(atlases_dir, "atlases.map"), "w") as atlases_map_writer:
        for file, sprites in atlases_data.items():
            atlases_map_writer.write(f":{file}\r\n")  # Game doesn't like it the endings aren't CRLF
            for sprite in sprites:
                atlases_map_writer.write(f"{sprite[0]} = {sprite[1]}\r\n")

    # Write our own atlas file
    ap_atlas_text = f":{AP_ATLAS_NAME}\r\n"
    for line in atlases_data[AP_ATLAS_NAME]:
        ap_atlas_text += f"{line[0]} = {line[1]}\r\n"
    with open(os.path.join(data_dir, "Atlases", f"{AP_ATLAS_NAME}.txt"), "w") as ap_atlas_writer:
        ap_atlas_writer.write(ap_atlas_text)
