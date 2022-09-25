# Hammerwatch

## Where is the settings page?

The [player settings page for this game](../player-settings) contains all the options you need to configure and export a config file.

## What does randomization do to this game?

The locations of most items have been swapped around. Logic is in place to ensure the game is always able to be
completed, however the player may need to go to certain areas before they would in the vanilla game.

## What is the goal of Hammerwatch when randomized?

Depending on the campaign you choose the goal is the same as in Vanilla, defeat the dragon in the Castle Hammerwatch campaign
or defeat Sha'Rand in the Temple of the Sun campaign!

## What items and locations get shuffled?

All pickups/valuables are shuffled except for coin piles, pots, crates, and bushes. Bonus chests and keys are
by default not shuffled due to the sheer number of junk items added to the pool, but this behavior can be toggled
in the YAML. Items from secrets and puzzles can also be included in the pool.

Hammerwatch in vanilla already implements some item randomization, and these rules are taken into account when determining which
locations can have items. This behavior can be adjusted in the player's YAML file.

## What items can appear in other players' worlds?

Any shuffled item can be in other players' worlds. It is possible to limit certain items to your own world.

## What does another world's item look like in Hammerwatch?

An item belonging to another player's world will have a sprite resembling the Archipelago logo. When picked up the item
it represents will automatically be sent to the other player.

## When the player receives an item, what happens?

When the player receives an item it appears at their feet, and they immediately pick it up if they can.