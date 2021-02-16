import random
import math
import sys
import os
from monster.monster import Monster, Monster_seed
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



if __name__ == '__main__':
    main()
    