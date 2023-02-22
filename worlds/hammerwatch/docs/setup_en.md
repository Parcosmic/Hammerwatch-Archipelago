# Hammerwatch Randomizer Setup Guide

## Required Software

- Hammerwatch: [Hammerwatch Steam Page](https://store.steampowered.com/app/239070/Hammerwatch/)
- HammerwatchAP Installer: [Download link coming soon!]
- Archipelago: [Archipelago Releases Page](https://github.com/ArchipelagoMW/Archipelago/releases).

## Hammerwatch Mod Installation Procedures

Download and extract the .zip file containing the installer and necessary files. Move all of these files into your
Hammerwatch install directory and run HammerwatchAPInstaller.exe. This will create a modded exe called
HammerwatchAP.exe. Run this to play using Archipelago, and launch the original exe to play without the mod.

To uninstall the mod run APModUninstall.bat to remove all mod files.

## Configuring your config (.yaml) file

### What is a config file and why do I need one?

See the guide for info about YAML files on the Archipelago setup guide: 
[Archipelago Setup Guide](/tutorial/Archipelago/setup/en)

### Where do I get a config file?

You can configure the settings for your game on the Player Settings page and export them as a config file.
Player settings page: [Hammerwatch Player Settings Page](/games/Hammerwatch/player-settings)

### Verifying your config file

To make sure your config file is formatted correctly you can check it on the YAML Validation page:
[YAML Validation page](/mysterycheck)

## Joining a multiworld game

1. Run HammerwatchAP.exe
2. Select "Archipelago" on the main menu
3. In the first field of the dialogue box enter the sever ip address together with the port (ex. archipelago.gg:38281)
4. In the second field enter your slot name
5. In the third field enter the server password if it has one, else leave it blank
6. Select "OK". After you have been connected verify that the correct information is shown on the main menu
7. Navigate the menus to set up playing the game as normal (note: selecting "Single" on the main menu will redirect
you to the Archipelago-specific menu)
8. After the level has generated you may select your hero's color, then select "Play" to start playing!

When later reconnecting to a server you have previously played on, if a save exists for that game it will automatically 
be loaded after selecting "OK". Alternatively, you can select an Archipelago save using "Load" on the main menu. This 
will automatically try to connect you to the server and load the game.

## Playing multiplayer (co-op)

Playing together in the same game is supported in the Archipelago randomizer. However, all clients playing together
should be connected to the same slot in Archipelago. Other than that, the procedure for playing multiplayer is the same
as in the vanilla game.
