import math
from randomization import dice

class AbilityGenerator(object):
    def __init__(self, abilities):
        self.abilities = abilities
        #super(AbilityGenerator, self).__init__(*args))
        

    # Generate core stats and ability bonuses
    def ability_generator(abilities=6):
        abilities = abilities
        scores = []
        modifiers = []
        roller = dice.Dice(256)
        
        for each in range(abilities):
            roll = roller.dice_roller(4, 6)
            roll.remove(min(roll))
            ability_score = 0
            for each in roll:
                ability_score = ability_score + each
            scores.append(ability_score)
            ability_modifier = math.floor((ability_score - 10) / 2)
            modifiers.append(ability_modifier)

        score_mod_pairs = list(zip(scores, modifiers))
        
        return score_mod_pairs