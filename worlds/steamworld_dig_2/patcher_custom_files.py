import os
from copy import deepcopy
import xml.etree.ElementTree as et

from . import assets, game_data
from .client_util import ClientContextData, create_node


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
    atlas_bytes = files(assets).joinpath(ap_atlas_png).read_bytes()
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


def patch_entities(data_dir: str, offworld_item_names: list[str]):
    pickups_file = os.path.join(data_dir, "Definitions", "entities.pickups.xml")
    pickups_doc = et.parse(pickups_file)
    pickups_root = pickups_doc.getroot()

    # Edit sprite of freestanding blueprints
    pickup_blueprint_node = pickups_root.find(".//Entity[@Name='pickup_blueprint']")
    pickup_blueprint_node.remove(pickup_blueprint_node.find("./RigidCharacter"))
    # blueprint_rigid_character_node = pickup_blueprint_node.find("./RigidCharacter/File")
    # blueprint_rigid_character_node.text = "Sprites/ElMachino/cog_03.irc2"
    pickup_blueprint_node.find("./LightComponent/Color").text = "1.0, 1.0, 1.0"
    blueprint_effect_node = create_node("Effect")
    blueprint_effect_node.append(create_node("ParticleEffect", text=game_data.UPGRADE_EFFECT))
    pickup_blueprint_node.append(blueprint_effect_node)

    # Floating offworld item to replace artifacts and containers
    ap_offworld_item_node = deepcopy(pickup_blueprint_node)
    ap_offworld_item_node.attrib["Name"] = game_data.AP_OFFWORLD_ITEM
    ap_offworld_item_node.find("./Effect/ParticleEffect").text = game_data.AP_CONTAINER_EFFECT
    pickups_root.append(ap_offworld_item_node)

    pickups_doc.write(pickups_file)

    editor_pickups_file = os.path.join(data_dir, "Definitions", "editor_pickups.xml")
    editor_pickups_doc = et.parse(editor_pickups_file)
    editor_pickups_root = editor_pickups_doc.getroot()

    editor_pickup_entries_to_add = [
        *game_data.in_game_item_data.keys(),
        *offworld_item_names,
    ]
    # Add custom blueprint pickup items
    for editor_string in editor_pickup_entries_to_add:
        if "collectible" in editor_string:
            continue
        editor_pickup_node = et.Element("EditorPickup")
        editor_pickup_node.attrib["Name"] = editor_string
        value_node = et.Element("Value")
        value_node.text = editor_string
        editor_pickup_node.append(value_node)
        editor_pickups_root.append(editor_pickup_node)

    editor_pickups_doc.write(editor_pickups_file)

    # Modify entity objects
    objects_file = os.path.join(data_dir, "Definitions", "entities.objects.xml")
    objects_doc = et.parse(objects_file)
    objects_root = objects_doc.getroot()

    teleporter_ap_object = deepcopy(objects_root.find("./Entity[@Name='teleporter']"))
    teleporter_ap_object.attrib["Name"] = "teleporter_ap"
    teleporter_blocker_info = teleporter_ap_object.find("./Blocker")
    teleporter_blocker_info.find("./ThemedBlockerEntities").clear()
    # teleporter_blocker_info.find("./UnblockBanner").attrib["IsTeleporter"] = "false"
    # teleporter_ap_object.remove(teleporter_blocker_info)
    objects_root.append(teleporter_ap_object)

    # Gotta build the spawner from scratch so it doesn't get frozen during cutscenes
    spawner_ap_object = et.Element("Entity", attrib={"Name": "spawner_ap", "Template": "triggered_arrow_shooter_single"})
    spawner_ap_object.append(et.Element("CutsceneFreeze", attrib={"Enable": "false"}))
    spawner_node = create_node("Spawner")
    spawner_node.append(et.Element("Spawn", attrib={"Offset": "0, 1"}))
    spawner_node.append(create_node("Interval", text="0"))
    spawner_node.append(create_node("StartActive", text="false"))
    spawner_node.append(create_node("DeactivateAfterActiveTime", text="true"))
    spawner_node.append(create_node("ActiveTime", text="0.1"))
    spawner_node.append(create_node("SpawnsPerActiveTime", text="1"))
    spawner_ap_object.append(spawner_node)
    physics_node = create_node("Physics")
    physics_node.append(create_node("CollisionType", text="ghost"))
    spawner_ap_object.append(physics_node)
    texture_node = create_node("Texture")
    texture_node.append(create_node("File", text=""))
    spawner_ap_object.append(texture_node)
    objects_root.append(spawner_ap_object)

    upgrade_cog_container = objects_root.find("./Entity[@Name='upgrade_cog_container']")

    # Create an empty cogbox to deliver upgrades in tandem with the mod
    cogbox_empty = deepcopy(upgrade_cog_container)
    cogbox_empty.attrib["Name"] = game_data.COGBOX_EMPTY
    cogbox_empty.remove(cogbox_empty.find("Drop"))
    cogbox_physics_node  = cogbox_empty.find("Physics")
    cogbox_physics_node.remove(cogbox_physics_node.find("FallDamage"))
    objects_root.append(cogbox_empty)

    # Create a cogbox that drops 4 super omni orbs like a container
    cogbox_super_orbs = deepcopy(upgrade_cog_container)
    cogbox_super_orbs.attrib["Name"] = game_data.COGBOX_SUPER_ORBS
    cogbox_super_orbs_drop_node = cogbox_super_orbs.find("Drop")
    cogbox_super_orbs_drop_node.remove(cogbox_super_orbs_drop_node.find("DropEntity"))
    cogbox_super_orbs_drop_node.append(et.Element("OrbCount", attrib={"All": "4"}))
    cogbox_super_orbs_physics_node  = cogbox_super_orbs.find("Physics")
    cogbox_super_orbs_physics_node.remove(cogbox_super_orbs_physics_node.find("FallDamage"))
    objects_root.append(cogbox_super_orbs)

    objects_doc.write(objects_file)


def patch_effects(data_dir: str):
    pickups_file = os.path.join(data_dir, "Effects", "pickups.pe")
    pickups_doc = et.parse(pickups_file)
    pickups_root = pickups_doc.getroot()

    ap_colors = {
        "0": "195, 117, 129",
        "0.167": "211, 160, 125",
        "0.333": "232, 228, 144",
        "0.5": "115, 194, 116",
        "0.667": "122, 120, 186",
        "0.833": "199, 143, 191",
    }
    ap_gradient = ""
    for key, col in ap_colors.items():
        ap_gradient += f"{key}:{col}, 182;"
    ap_gradient += f"1:{ap_colors['0']}, 182"

    super_omni_container_effect_node = None
    for particle_effect in pickups_root:
        name_node = particle_effect.find("Name")
        if name_node is None:
            continue
        if name_node.text == "all_resource":
            super_omni_container_effect_node = particle_effect
            break

    if super_omni_container_effect_node is None:
        print("Couldn't find Super Omni Orb Container particle effect node!!")
        return

    ap_particle_effect_node = deepcopy(super_omni_container_effect_node)
    ap_particle_effect_node.find("Name").text = game_data.AP_CONTAINER_EFFECT
    children_node = ap_particle_effect_node.find("Children")
    core_gem_node = children_node[0]
    core_gem_node.find("./Parameters/Parameter/Value").text = "Textures/Pickups/ap_container_core"
    for parameter in core_gem_node.find("Parameters"):
        param_name = parameter.find("Name").text
        if param_name == "EmitterInitialRotationSpeed":
            parameter.find("Value").text = "0"
    glow_node = children_node[3]
    for parameter in glow_node.find("Parameters"):
        param_name = parameter.find("Name").text
        if param_name == "ParticleColor":
            parameter.find("Value").text = ap_gradient
    children_node.remove(children_node[2])
    pickups_root.append(ap_particle_effect_node)

    upgrade_particle_effect_node = deepcopy(ap_particle_effect_node)
    upgrade_particle_effect_node.find("Name").text = game_data.UPGRADE_EFFECT
    children_node = upgrade_particle_effect_node.find("Children")
    core_gem_node = children_node[0]
    core_gem_node.find("./Parameters/Parameter/Value").text = "Textures/Pickups/upgrade_container_core"
    case_node = children_node[1]
    case_node.find("./Parameters/Parameter/Value").text = "Textures/Pickups/fire_case"
    glow_node = children_node[2]
    for parameter in glow_node.find("Parameters"):
        param_name = parameter.find("Name").text
        if param_name == "ParticleColor":
            parameter.find("Value").text = "0:255, 255, 255, 255;1:255, 255, 255, 255"
    pickups_root.append(upgrade_particle_effect_node)

    pickups_doc.write(pickups_file)

    # Add our custom particles to the definitions file
    particles_file = os.path.join(data_dir, "Definitions", "particles.xml")
    particles_doc = et.parse(particles_file)
    particles_root = particles_doc.getroot()

    new_particles = [
        game_data.AP_CONTAINER_EFFECT,
        game_data.UPGRADE_EFFECT,
    ]

    for particle in new_particles:
        particles_root.append(create_node("ParticleEffect", name=particle))

    particles_doc.write(particles_file)
