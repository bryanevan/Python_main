import pickle


def display_recipe(recipe):
    print("Recipe Name:", recipe["name"])
    print("Cooking Time:", recipe["cooking_time"], "minutes")
    print("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print("-", ingredient)
    print("Difficulty:", recipe["difficulty"])
    print("-" * 30)


def search_ingredient(data):
    # print the list of ingredients
    print("Available ingredients:")
    for index, ingredient in enumerate(data["all_ingredients"]):
        print(index, ingredient)
    print("-" * 30)
    # ask user for the ingredient they want to search for
    try:
        ingredient_searched = data["all_ingredients"][
            int(input("Enter the number of the ingredient you want to search for: "))
        ]
    except:
        print("Incorrect input")
        return
    else:
        # search for recipes containing the ingredient
        recipes_found = []
        for recipe in data["recipes_list"]:
            if ingredient_searched in recipe["ingredients"]:
                recipes_found.append(recipe)
        # display the recipes found
        for recipe in recipes_found:
            display_recipe(recipe)


# Main code

# ask user for the name of the file containing the recipes
filename = input("Enter the filename where you've stored your recipes: ")

try:
    file = open(filename, "rb")
    data = pickle.load(file)
except FileNotFoundError:
    print("File doesn't exist")
else:
    search_ingredient(data)
finally:
    print("Goodbye!")
    file.close()
