"""
This defines the classes to handle monster stats 
"""

class monster:
    def __init__(self, name):
        self.name = name
        #self.description = []
        self.hit_dice = []
        self.core_ability = []

    def update_base_stats(self, hit_dice, core_scores):
        self.hit_dice.append(hit_dice)
        self.core_ability = core_scores


class monster_seed:
    def __init__(self, name, hit_dice, abilities):
        self.name = name
        self.hit_dice = hit_dice
        self.abilities = abilities
        self.ability_set = []
        # self.coreAbilityBlock

    def core_stats(self, ability_results):
        self.ability_set = list(zip(self.abilities, ability_results))


        