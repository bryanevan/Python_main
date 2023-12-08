import pickle


def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = []
    while True:
        ingredient = input("Enter an ingredient _ enter 'x' when done:")
        if ingredient == "x":
            break
        else:
            ingredients.append(ingredient)

    # Recipe Dictionary
    recipe_dict = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
    }
    difficulty = calc_difficulty(recipe_dict)
    recipe_dict["difficulty"] = difficulty
    return recipe_dict


def calc_difficulty(recipe):
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        difficulty = "Easy"
    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        difficulty = "Medium"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"
    return difficulty


# Main Code

filename = input("Enter the filename of the binary file to load: ")
try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
        print("Data loaded successfully.")
except FileNotFoundError:
    print("File not found. Creating a new data structure.")
    data = {"recipes_list": [], "all_ingredients": []}
except pickle.PickleError as e:
    print("Error loading data from file:", e)
    print("Creating a new data structure.")
    data = {"recipes_list": [], "all_ingredients": []}
else:
    file.close()  # Close the file stream
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]


n = int(input("How many recipes would you like to add? "))

# Input recipes
for _ in range(n):
    recipe = take_recipe()

    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
    recipes_list.append(recipe)

data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}

# Save data to a binary file using pickle
filename = input("Enter the filename for saving the data: ")
with open(filename, "wb") as file:
    pickle.dump(data, file)
    print("Data saved to", filename)
    file.close()
