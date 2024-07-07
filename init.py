'''
    init.py

    has on_start


'''

from libraries import *


Cookbook1a = {  "spicy": [],
                "sour": [],
                "sweet": [],
                "salty": [],
                "cold": [],
                "hot": [],
                "extreme": [],
                "raw": [],
                "greasy": [],
                "fried": [],
                "savory": [],
                "badluck": []
              }
Cookbook1b = {  "spicy": [],
                "sour": [],
                "sweet": [],
                "salty": [],
                "cold": [],
                "hot": [],
                "extreme": [],
                "raw": [],
                "greasy": [],
                "fried": [],
                "savory": [],
                "badluck": []
              }

Characters = {
                "geb": None,
                "yisang": None,
                "yigeum": None,
                "beth": None,
                "ludmila": None,
                "montag": None,
                "gahwan": None,
                "fleur": None,,
                "honglu": None,
                "ming": None,
                "heath": None

            }
recipe = []

@bot.event
async def on_ready():

    # cookbooks init
    cookbook1a_raw = gs.get('Cookbook(1a)', 'A1:Z12')
    cookbook1b_raw = gs.get('Cookbook(1b)', 'A1:Z12')

    for i in range(0, len(cookbook1a_raw)):
        row_a = cookbook1a_raw[i]
        row_b = cookbook1b_raw[i]
        Cookbook1a[row_a[0]] = row_a[1:]
        Cookbook1b[row_b[0]] = row_b[1:]

    # character init
    character_raw = gs.get('Character Status', 'A2:L44')

    for i in range(0, len(character_raw), 4):
        row = character_raw[i]
        code_name = row[0]
        name = row[1]
        full_name = row[2]
        row_num = i+2
        hp = int(row[5])
        hunger = int(row[6])
        food_stats = row[7].split()
        food_stats[1] = int(food_stats[1])
        food_stats[2] = int(food_stats[2])
        like_food = row[8].split()
        hate_food = row[9]
        money = int(row[10])
        vitality = int(row[11])
        Characters[code_name] = Character(name, full_name, row, hp, hunger, food_stats, like_food, hate_food, money, vitality)

        print(f"{Characters[code_name].name}\n")

    # recipe init
    recipe_names_raw = gs.get('Cookbook(recipe)', 'A2:A')
    for name in recipe_names_raw:
        recipe.append(name[0])
    
    print(Recipe(recipe[0], 0))






    print(f'{bot.user.name} -- finished')


