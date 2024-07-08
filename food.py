
from enum import Enum
import google_sheets as gs

class FoodStage(Enum):
    process1 = "P1"
    process1_awaiting = "P1_W"
    process2 = "P2"
    process2_awaiting = "P2_W"
    process1a = "P1A"
    process1a_awating = "P1A_W"
    process1b = "P1B"
    process1b_awaiting = "P1B_W"

class FoodText(Enum):
    success = ""
    fail = ""

class State_PrepFood:

    # pass in the whole character object for maker
    def __init__(self, name, num, maker):
        self.recipe = Recipe(name, num)
        self.vitality_restore = recipe.vitality_restore
        self.trait1 = ""
        self.trait2 = ""
        self.additional_food = ""
        self.current = FoodStage.process1.value
        self.maker = maker

    # returns text to be printed and changes stuff accordingly
    # the accepting end will handle stage deletion and rolling of the dice
    # arg will be a dice roll if it exists (number), positive for roll, -1 for opt out  

    def run(self, roll):

        c = self.maker.name

        # start 
        if (self.current == FoodStage.process1.value):
            self.current = FoodStage.process1_awaiting.value
            return self.recipe.process1.replace('{c}', c)

        # start -> onto 1a, opt out not possible
        elif (self.current == FoodStage.process1_awaiting.value):

            self.current = FoodStage.process1a.value

            # write something more for actually leading into 1a (and 1b too)
            if (roll >= self.difficulty):
                return self.recipe.process1_success
            else:
                return self.recipe.process1_fail

        # 1a
        elif (self.current == FoodStage.process1a.value):
            return ""

        # 1a -> 1b, opt out possible
        elif (self.current == FoodStage.process1a_awaiting.value):
            return ""

        # 1b
        elif (self.current == FoodStage.process1b.value):
            return ""

        # 1b -> 2, opt out possible
        elif (self.current == FoodStage.process1b_awaiting.value):
            return ""

        # 2
        elif (self.current == FoodStage.process2.value):
            return ""

        # 2 -> end, opt out not possible
        elif (self.current == FoodStage.process2_awaiting.value):
            return ""

        return ""
    




class Recipe:
    def __init__(self, name, num):
        self.name = name
        self.row_num = num+2
        row = gs.get('Cookbook(recipe)', f'A{self.row_num}:I{self.row_num}')[0]

        self.vitality_restore = int(row[1])
        self.difficulty = int(row[2])
        self.process1 = row[3]
        self.process1_success = row[4]
        self.process1_fail = row[5]
        self.process2 = row[6]
        self.process2_success = row[7]
        self.process2_fail = row[8]

    def __str__(self):
        return f"name: {self.name}\nrow_num: {self.row_num}\nvitality_restore: {self.vitality_restore}\ndifficulty: {self.difficulty}\nprocess1: {self.process1}\nprocess2: {self.process2}\n"

class Edible:
    def __init__(self, name):
        pass
    def __str__(self):
        return ""
