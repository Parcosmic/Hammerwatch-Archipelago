"""
Extractor for Hammerwatch map files
Place an extracted map folder named "map" in this same directory
"""
import os
import io
import xml.etree.ElementTree as ET
import typing

# from .Items import ItemData
from Names import ItemName


xml_name = {
    ItemName.bonus_chest: "items/bonus_chest.xml",
    ItemName.bonus_key: "items/bonus_key.xml",
    ItemName.chest_blue: "items/chest_blue.xml",
    ItemName.chest_green: "items/chest_green.xml",
    ItemName.chest_red: "items/chest_red.xml",
    ItemName.chest_wood: "items/chest_wood.xml",
    ItemName.vendor_coin: "items/collectable_1.xml",
    ItemName.plank: "items/collectable_2.xml",
    ItemName.key_bronze: "items/key_bronze.xml",
    ItemName.key_silver: "items/key_silver.xml",
    ItemName.key_gold: "items/key_gold.xml",
    ItemName.mirror: "items/key_mirror.xml",
    ItemName.ore: "items/key_ore.xml",
    ItemName.key_teleport: "items/key_teleport.xml",
    ItemName.ankh: "items/powerup_1up.xml",
    ItemName.ankh_5up: "items/powerup_5up.xml",
    ItemName.potion_damage: "items/powerup_potion1.xml",
    ItemName.potion_rejuvenation: "items/powerup_potion2.xml",
    ItemName.potion_invulnerability: "items/powerup_potion3.xml",
    ItemName.stat_upgrade_damage: "items/upgrade_damage.xml",
    ItemName.sonic_ring: "items/special_ring.xml",
    ItemName.serious_health: "items/special_serious_health.xml",
    ItemName.pickaxe: "items/tool_pickaxe.xml",
    ItemName.diamond: "items/valuable_diamond.xml",
    ItemName.diamond_red: "items/valuable_diamond_red.xml",
    ItemName.diamond_small: "items/valuable_diamond_small.xml",
    ItemName.diamond_small_red: "items/valuable_diamond_small_red.xml",
    ItemName.stat_upgrade: "prefabs/upgrade_random.xml"
}

item_name = {v: k for k, v in xml_name.items()}


def load_items(xmlfile, item_hwids: typing.Dict[str, typing.List[typing.Tuple[int, str]]]):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    for itemcategory in root.findall("./dictionary[@name='items']/array"):
        xml_type = itemcategory.attrib.pop("name")
        if xml_type not in randomized_items:
            continue
        type = item_name[xml_type]
        if xml_name[type] not in item_hwids:
            item_hwids[type] = []
        for item in itemcategory.findall("array"):
            hwid = int(item.find("int").text)
            pos = item.find('vec2').text
            # print(f"id: {hwid}, pos: {pos}")
            # loaded_items.append(ItemData(0x130000 + int(item.find("int").text)))
            item_hwids[type].append((hwid, pos))
    # return loaded_items


randomized_items = {
    # "items/bonus_chest.xml",
    # "items/bonus_key.xml",
    "items/chest_blue.xml",
    "items/chest_green.xml",
    "items/chest_purple.xml",
    "items/chest_red.xml",
    "items/chest_wood.xml",
    "items/collectable_1.xml",
    "items/collectable_2.xml",
    "items/collectable_4.xml",
    "items/key_bronze.xml",
    "items/key_silver.xml",
    "items/key_gold.xml",
    "items/powerup_1up.xml",
    "items/powerup_5up.xml",
    "items/powerup_7up.xml",
    "items/powerup_health.xml",
    "items/powerup_potion1.xml",
    "items/powerup_potion2.xml",
    "items/powerup_potion3.xml",
    "items/special_ring.xml",
    "items/special_serious_health.xml",
    "items/tool_lever.xml",
    "items/tool_pan.xml",
    "items/tool_pickaxe.xml",
    "items/tool_shovel.xml",
    "items/upgrade_damage.xml",
    "items/upgrade_damage_2.xml",
    "items/upgrade_defense.xml",
    "items/upgrade_defense_2.xml",
    "items/upgrade_health.xml",
    "items/upgrade_health_2.xml",
    "items/upgrade_mana.xml",
    "items/upgrade_mana_2.xml",
    "items/valuable_diamond.xml",
    "items/valuable_diamond_red.xml",
    "items/valuable_diamond_small.xml",
    "items/valuable_diamond_small_red.xml",
    "items/key_mirror.xml",
    "items/key_ore.xml",
    "items/key_teleport.xml",
}

door_items = {
    "items/bonus_door_h_32.xml",
    "items/bonus_door_v_32.xml",
    "items/door_a_bronze_h.xml",
    "items/door_a_bronze_h_cap_l.xml",
    "items/door_a_bronze_h_cap_r.xml",
    "items/door_a_bronze_h_v2.xml",
    "items/door_a_bronze_v.xml",
    "items/door_a_bronze_v_v2.xml",
    "items/door_a_bronze_v_cap_up.xml",
    "items/door_a_silver_h.xml",
    "items/door_a_silver_h_cap_l.xml",
    "items/door_a_silver_h_cap_r.xml",
    "items/door_a_silver_h_v2.xml",
    "items/door_a_silver_v.xml",
    "items/door_a_silver_v_v2.xml",
    "items/door_a_silver_v_cap_up.xml",
    "items/door_a_gold_h.xml",
    "items/door_a_gold_h_cap_l.xml",
    "items/door_a_gold_h_cap_r.xml",
    "items/door_a_gold_h_v2.xml",
    "items/door_a_gold_v.xml",
    "items/door_a_gold_v_v2.xml",
    "items/door_a_gold_v_cap_up.xml",
    "items/door_g_silver_h.xml",
    "items/door_g_silver_h_cap_l.xml",
    "items/door_g_silver_h_cap_r.xml",
    "items/door_g_silver_h_v2.xml",
    "items/door_g_gold_h.xml",
    "items/door_g_gold_h_cap_l.xml",
    "items/door_g_gold_h_cap_r.xml",
    "items/door_g_gold_h_v2.xml",
}

randomized_prefabs = {
    "prefabs/upgrade_random.xml"
}


def main():
    dir_name = "map"
    files = os.listdir(f"./{dir_name}")
    files = ["level_hub.xml"]
    item_hwids: typing.TypedDict[str, typing.List[int]] = {}
    for level in files:
        print(level)
        load_items(f"{dir_name}/{level}", item_hwids)

    print("Totals:")
    sum = 0
    for item in sorted(item_hwids.keys()):
        hwids = item_hwids.get(item)
        print(f"{item} - {len(hwids)}")
        sum += len(hwids)
        # for hwid in hwids:
            # print(f"    {hwid}")
    print(f"Total Items: {sum}")


if __name__ == "__main__":
    main()
