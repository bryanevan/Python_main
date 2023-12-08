recipe_1 = {
    "name": "Tea",
    "cooking_time":5,
    "ingredients": ["Tea Leaves", "Sugar", "Water"],
    }

recipe_2 = {
    "name": "Iced Latte",
    "cooking_time":3,
    "ingredients": ["Coffee Grinds", "Milk", "Ice"],
    }

recipe_3 = {
    "name": "Pancakes",
    "cooking_time":10,
    "ingredients": ["Flour", "Water", "Butter"],
    }

recipe_4 = {
    "name": "Waffles",
    "cooking_time":7, 
    "ingredients": ["Sugar", "Spice", "Everything Nice"],
    }

recipe_5 = {
    "name": "Eggs",
    "cooking_time":5,
    "ingredients": ["Egg Whites", "Joy", "Oil"],
    }

all_recipes = [recipe_1, recipe_2, recipe_3, recipe_4, recipe_5]

for recipe in all_recipes:
    print("Ingredients for", recipe["name"], ":", recipe["ingredients"])
