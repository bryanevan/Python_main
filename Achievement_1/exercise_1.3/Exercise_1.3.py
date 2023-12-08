recipes_list = []
ingredients_list = []


def take_recipe():
    # Input from the user
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients, separated by commas: ").split(',')
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    return recipe

# Ask the user how many recipes they want to enter
n = int(input("How many recipes would you like to enter? "))

# Update recipe_list
for _ in range(n):
    recipe = take_recipe()
    # Update ingredient_list
    for ingredient in recipe["ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

    # Set the difficulty of the recipe
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = "Easy"
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = "Medium"
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = "Intermediate"
    else:
        recipe['difficulty'] = "Hard"


# print("Recipes List:", Recipes_list)
print("Recipes List:", recipes_list)

# print list of ingredients across all recipes A-Z
print("Ingredients Available Across All Recipes")
print("----------------------------------------")

ingredients_list.sort()
for ingredient in ingredients_list:
    print(ingredient)