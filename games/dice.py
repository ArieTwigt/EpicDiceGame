import random

# define the Dice class
class Dice:

    # constructor
    def __init__(self, 
                 max_score:int, 
                 color:str ="white"):
        # check for the right type
        if type(max_score) is not int:
            raise TypeError("Max score should be an integer.")
        
        # check if the value is not negative
        if max_score <=0:
            raise ValueError("Turns should be higher than 0.")
        
        self.max_score = max_score
        self.color = color

    
    # method to throw the dice
    def throw(self):
        # increase the max score with 1, for range
        max_throw = self.max_score + 1

        # create the possible scores
        possible_scores = range(1, max_throw)

        # select from the possible scores
        score = random.choice(possible_scores)
        print(f"You threw: {score} 🎲")
        return score
    

class RegularDice(Dice):
    pass


class DoubleDice(Dice):
    def throw(self):
        # increase the max score with 1, for range
        max_throw = self.max_score + 1

        # create the possible scores
        possible_scores = range(1, max_throw)

        # select from the possible scores
        score = random.choice(possible_scores) * 2
        print(f"You threw: {score} 🎲")
        return score


    def regular_throw(self):
        super().throw()