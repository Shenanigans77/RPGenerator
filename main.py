import random
import math
import sys
import os
import monster
import unittest
 
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
    Starter = os.urandom(256)
    random.seed(a=Starter)

    hdFromCsv = [4, 6, 5]
    abilitiesFromCsv = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

    # Initialize monster seed 
    newMonster = monster.monster_seed("Dave", hdFromCsv, abilitiesFromCsv)
    newMonster.core_stats(ability_generator(abilities=len(newMonster.abilities)))
    print("{}".format(newMonster.ability_set))
    
    Stat = dice_roller(3,6,4)
    # Kind of ugly, should be a better way to do this.
    print("HP is {} ({}d{} +{})".format(
        Stat[0],Stat[1],Stat[2],Stat[4]
        ))
    print("Rolls: {}".format(Stat[3]))
    Abilities = ability_generator()
    print("Scores: {}".format(Abilities))

# Generate core stats and ability bonuses
def ability_generator(abilities=6):
    """Generates a specified number of abilities and modifiers.
    
    Keyword Arguments:
        abilities {int} -- [description] (default: {6})

    Generate standard ability set
    >>> random.seed(a=10)
    >>> ability_generator()
    [(13, 1), (11, 0), (13, 1), (12, 1), (11, 0), (11, 0)]
    """
    abilities = abilities
    scores = []
    modifiers = []
    
    for each in range(abilities):
        roll = dice_roller(4, 6)[3]
        roll.remove(min(roll))
        ability_score = 0
        for each in roll:
            ability_score = ability_score + each
        scores.append(ability_score)
        ability_modifier = math.floor((ability_score - 10) / 2)
        modifiers.append(ability_modifier)

    score_mod_pairs = list(zip(scores, modifiers))
    
    return score_mod_pairs

# Generate dice-based values
def dice_roller(dice, size, modifier=0):
    """A die roller for generating numerical monster stats
    
    Arguments:
        dice {int} -- The number of dice to use
        size {int} -- The size of the dice, e.g. 6 for a six-sided die
    
    Keyword Arguments:
        modifier {int} -- A modifier for the rolls.
        This is added to each roll (default: {0})
    
    Returns:
        [list] -- A list of the total rolled, number of dice, 
        size of each die, value of each roll, and any modifier applied.

    Result with 4d8 no modifier
    >>> random.seed(a=10) # Sets the random seed consistent for repeatable testing
    >>> dice_roller(4, 8)
    [17, 4, 8, [1, 7, 8, 1]]

    Result with 3d10, +2 modifier
    >>> dice_roller(3, 10, 2)
    [26, 3, 10, [6, 10, 10], 2]
    """
    Dice = dice
    Modifier = modifier
    Score = 0
    Rolls = []
    for die in range(Dice):
        Die = random.randint(1, size) + Modifier
        Rolls.append(Die)
        Score = Score + Die
    die_stats = [Score, dice, size, Rolls]
    if Modifier != 0:
        die_stats.append(Modifier)

    return die_stats

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

class TestDiceRoller(unittest.TestCase):

    def setUp(self):
        self.randomSeed = random.seed(a=10)

    def test_roll_default(self):
        self.assertEqual(dice_roller(4, 8), [17, 4, 8, [1, 7, 8, 1]])
    
    def test_roll_modified(self):
        self.assertEqual(dice_roller(3, 10, 2), [26, 3, 10, [6, 10, 10], 2])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    unittest.main()
    main()
    