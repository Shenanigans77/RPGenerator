import random
import os
# Handles dice rolling. Instantiated with a random seed for consistency
class Dice(object):
    def __init__(self, seed):
        self.seed = os.urandom(seed)
        self.modifier = 0
        self.rolls = []
        self.num_dice = 0
        self.die_size = 0 

    def roll_total(self, faces, number, modifier=0):
        Number = number
        Faces = faces
        mod = modifier
        total = 0
        try:
            for each in range(Number):
                roll = random.randint(1, Faces) + mod
                #print("{}", roll)
                total += roll
            return total
        except:
            pass

        
    def dice_roller(self, dice, size, modifier=0):
        """dice_roller takes arguments for the number of dice you want
        to roll and the size of the dice. There is also an option to add a modifier.

        Args:
            dice (int): The number of dice to roll.
            size (int): The number of die faces for each die.
            modifier (int, optional): Added to the total roll. Defaults to 0.

        Returns:
            int: Returns the total number rolled, including any modifiers 
        """
        Dice = dice
        Modifier = modifier
        Score = 0
        Rolls = []
        try:
            for die in range(Dice):
                Die = random.randint(1, size + 1) + Modifier
                Rolls.append(Die)
                Score = Score + Die

            self.roll_stats = [Score, Dice, size, Rolls]

            if Modifier != 0:
                self.roll_stats.append(Modifier)
            return Score
        except:
            pass


    # ? Is this method really necessary?
    # ? Does better comments really work?   
    def roll_stats(self):
        """Gets the number of dice, die size, rolls, and modifiers 
        from a die roll.

        Returns:
            List: die size, number of dice, values rolled, modifiers
        """
        return [self.die_size, self.num_dice, self.rolls, self.modifier]    