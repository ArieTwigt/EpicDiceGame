from games.dice import Dice
from typing import Literal


class Game:

    def __init__(self, 
                 max_turns:int,
                 dice: Dice ):
        self.max_turns = max_turns
        self.dice = dice
        self.turn_count = 0
        self.score = 0
        self.throws = []
        self.status: Literal["In progress", "Finished"] = "In progress"


    def take_turn(self):
        if self.turn_count < self.max_turns:
            result = self.dice.throw()

            # append the result
            self.throws.append(result)

            # increase the score
            self.score += result

            # increase the turn count
            self.turn_count += 1

            # show the score
            print(f"Score: {self.score}")

            if self.turn_count == self.max_turns:
                self.status = "Finished"
                total_score = self.__show_score()
                print(f"Total_score {total_score}")
                print("🏁 Finish")
         
        else:
            print("Game is already over")


    def __show_score(self):
        total_score = sum(self.throws)
        return total_score


    def __repr__(self):
        description = f"{self.status} - {self.turn}"
        return description
