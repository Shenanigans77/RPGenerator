import random
import math
import sys
import os
import monster
import unittest

from randomization.dice import Dice
 
# A procedural generator for RPG enemies
# This function should accept a set of parameters that need values
# These values are either numerical or 
# chosen from a set of available text values
def main():
    """
    RPGenerator takes a request for a stat block and 
    procedurally generates that stat block for the requested
    monster or monsters
    """
    # Initialize random generator
    # Starter = os.urandom(256)
    # random.seed(a=Starter)

    hdFromCsv = [4, 6, 5]
    abilitiesFromCsv = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

    # Initialize monster seed 
    newMonster = monster.Monster_seed("Dave", hdFromCsv, abilitiesFromCsv)
    newMonster.core_stats(ability_generator(abilities=len(newMonster.abilities)))
    print("{}".format(newMonster.ability_set))
    roller = Dice(256)
    
    Stat = roller.dice_roller(3,6,4)
    # Kind of ugly, should be a better way to do this.
    print("HP is {} ({}d{} +{})".format(
        Stat[0],Stat[1],Stat[2],Stat[4]
        ))
    print("Rolls: {}".format(Stat[3]))
    Abilities = ability_generator()
    print("Scores: {}".format(Abilities))

# Generate core stats and ability bonuses
def ability_generator(abilities=6):
    abilities = abilities
    scores = []
    modifiers = []
    
    for each in range(abilities):
        roll = roller.dice_roller(4, 6)[3]
        roll.remove(min(roll))
        ability_score = 0
        for each in roll:
            ability_score = ability_score + each
        scores.append(ability_score)
        ability_modifier = math.floor((ability_score - 10) / 2)
        modifiers.append(ability_modifier)

    score_mod_pairs = list(zip(scores, modifiers))
    
    return score_mod_pairs


# Pick feats from a list and obey prerequisite requirements
def feat_picker(feat_list, feat_slots):
    #TODO
    return True

# Pick skills and allocate skill points
def skills_picker(max, points, skills):
    #TODO
    return True

# Optional: Pick equipment (not sure if this is overkill)
 
# Optional: Generate loot - everyone loves loot
def loot_generator(level):
    #TODO
    return True

if __name__ == '__main__':
    main()
    