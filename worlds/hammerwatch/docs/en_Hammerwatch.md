# Hammerwatch

## Where is the settings page?

The [player settings page for this game](../player-settings) contains all the options you need to configure and export 
a config file.

## What does randomization do to this game?

The locations of most items have been shuffled around. Logic is in place to ensure the game can always be completed, 
however the player may have to travel to areas in a different order they would normally have to in a vanilla game.

## What is the goal of Hammerwatch when randomized?

There are a few goals that can be chosen in your YAML:
* Defeat Worldfire the dragon in the Castle Hammerwatch campaign
* Defeat Worldfire and collect 12 strange planks, then escape with your life in the Castle Hammerwatch campaign
* Defeat Sha'Rand in the Temple of the Sun campaign
* Unlock and complete the Pyramid of fear in the Temple of the Sun campaign
* Collect a certain number of strange planks in either campaign

## What items and locations get shuffled?

All pickups/valuables are shuffled except for coin piles, pots, crates, and bushes. Recovery items 
(apples, mana crystals, etc.) and bonus chests are by default not shuffled due to the sheer number of junk items added 
to the pool, but this behavior can be toggled in the YAML. 
Items from secrets and puzzles can also be included in the pool.

In the Temple of the Sun campaign the frying pan, pumps lever, and pickaxe can be split into fragments. This requires 
you to collect all the fragments to get the full item. This makes it so you potentially have to explore more of the 
multiworld to progress more in your own game. This feature can be configured in the YAML.

Hammerwatch in vanilla already implements some item randomization, and these rules are taken into account when
determining which locations can have items.

## What does another world's item look like in Hammerwatch?

An item belonging to another player's world will have a sprite resembling the Archipelago logo. Depending on the type of
item it will have a different sprite to help let you know if a particularly difficult check may be worth it or not.
When picked up the item it represents will automatically be sent to the other player.

## When the player receives an item, what happens?

When the player receives an item it appears at their feet, and they immediately pick it up if they can. If the item is a
chest it is automatically broken open on delivery.

## If I'm at full health/mana how does the server know that I found a recovery item if I can't pick it up?

Items that can't be picked up can be walked on to notify the server that you have found the item. 
This prevents you from having to damage yourself or use a skill in order to collect the check and potentially get 
hint points!

## What are big bronze keys?

Big bronze keys are custom items created for the Castle Hammerwatch campaign. When picked up they act as 5 bronze keys.
They exist as an option to reduce the massive amount of required progression items in the item pool and to make
receiving bronze keys feel more meaningful.