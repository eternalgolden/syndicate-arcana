
from enum import Enum
import google_sheets as gs

class Stage(Enum):
    process1 = "P1"
    process2 = "P2"
    process1a = "P1A"
    process1b = "P1B"

class State_PrepFood:
    def __init__(self, name, num, maker_name):
        self.recipe = Recipe(name, num)
        self.vitality_restore = recipe.vitality_restore
        self.trait1 = ""
        self.trait2 = ""
        self.additional_food = ""
        self.current = Stage.process1.value
        self.maker = maker_name

    def run(args):
        pass
    







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
