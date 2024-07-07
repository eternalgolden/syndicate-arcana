'''
    character.py

'''
from libraries import *

class Character:
    def __init__(self, name, full_name, row, hp, hunger, food_stats, like_food, hate_food, money, vitality): 
        self.name = name
        self.full_name = full_name
        self.row = row
        self.hp = hp
        self.hunger = hunger
        self.food_stats = food_stats
        self.like_food = like_food
        self.hate_food = hate_food
        self.money = money
        self.vitality = vitality
        self.state = None


    def __str__(self):
        return ""
