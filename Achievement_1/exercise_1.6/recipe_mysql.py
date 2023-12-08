import mysql.connector

# Connect to the database
conn = mysql.connector.connect(host="localhost", user="cf-python", passwd="password")

# Create a cursor
cur = conn.cursor()

# Create a database
cur.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Use the database
cur.execute("USE task_database")

# Create a table called Recipes
cur.execute(
    "CREATE TABLE IF NOT EXISTS Recipes ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "name VARCHAR(50),"
    "ingredients VARCHAR(255),"
    "cooking_time INT,"
    "difficulty VARCHAR(20)"
    ")"
)


# spacer for readability
def space():
    print("-"*35)


# Main menu function.
def main_menu(conn, cur):
    while True:
        space()
        print("Main Menu:")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. View all recipes")
        print("6. Exit")
        space()

        try:
            selection = int(input("Your choice: "))
            if selection == 1:
                create_recipe(conn, cur)
            elif selection == 2:
                search_recipe(cur)
            elif selection == 3:
                update_recipe(conn, cur)
            elif selection == 4:
                delete_recipe(conn, cur)
            elif selection == 5:
                view_recipes(cur)
            elif selection == 6:
                conn.commit()
                conn.close()
                exit()
            else:
                space()
                print("Please select a valid option")
        except ValueError:
            space()
            print("Please select a valid option")


# Create a new recipe.
def create_recipe(conn, cur):
    ingredients = []
    name = input("\nEnter the name of the recipe: ")
    cooking_time = int(input("\nEnter the cooking time in minutes: "))
    ingredient = input("Enter an ingredient or type 'done' to finish: ")
    while ingredient != "done":
        ingredients.append(ingredient)
        ingredient = input("Enter an ingredient or type 'done' to finish: ")
    difficulty = calculate_difficulty(cooking_time, ingredients)
    ingredients = ", ".join(ingredients)
    cur.execute(
        "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)",
        (name, ingredients, cooking_time, difficulty),
    )
    conn.commit()
    space()
    print("Recipe created successfully!")


# Calculate the difficulty of a recipe based on its cooking time and number of ingredients.
def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"


# Search for a recipe based on an ingredient.
def search_recipe(cur):
    cur.execute("SELECT ingredients FROM Recipes")
    results = cur.fetchall()
    all_ingredients = []
    for row in results:
        for ingredient in row:
            ingredients_list = ingredient.split(
                ", "
            )  # Split the ingredients string into a list
            for item in ingredients_list:
                if item not in all_ingredients:
                    all_ingredients.append(item)
    space()
    print("Available ingredients:")
    space()
    for i in range(len(all_ingredients)):
        print(f"{i+1}. {all_ingredients[i]}")
    while True:
        try:
            ingredient_choice = int(
                input("\nEnter the number of the ingredient you want to search for: ")
            )
            if ingredient_choice not in range(1, len(all_ingredients) + 1):
                space()
                print("Please select a valid option")
            else:
                break
        except ValueError:
            space()
            print("Please select a valid option")
    search_ingredient = all_ingredients[ingredient_choice - 1]
    cur.execute(
        "SELECT name, ingredients, cooking_time, difficulty FROM Recipes WHERE ingredients LIKE %s",
        (f"%{search_ingredient}%",),
    )
    results = cur.fetchall()
    if len(results) == 0:
        space()
        print("No recipes found")
    else:
        space()
        print("Search results:")
        for row in results:
            space()
            print(f"Name: {row[0]}")
            print(f"Ingredients: {row[1]}")
            print(f"Cooking time: {row[2]} minutes")
            print(f"Difficulty: {row[3]}")


# update an existing recipe.
def update_recipe(conn, cur):
    results = cur.execute("SELECT * FROM Recipes")
    results = cur.fetchall()
    space()
    print("Available recipes:")
    for row in results:
        print(f"{row[0]}. {row[1]}")
    while True:
        try:
            recipe_choice = int(
                input("\nEnter the number of the recipe you want to update: ")
            )
            if recipe_choice not in range(1, len(results) + 1):
                space()
                print("Please select a valid option")
            else:
                break
        except ValueError:
            space()
            print("Please select a valid option")
    recipe_id = results[recipe_choice - 1][0]
    space()
    print("1. Name")
    print("2. Cooking time")
    print("3. Ingredients")
    while True:
        try:
            column_choice = int(
                input("\nEnter the number of the column you want to update: ")
            )
            if column_choice not in range(1, 4):
                space()
                print("Please select a valid option")
            else:
                break
        except ValueError:
            space()
            print("Please select a valid option")
    if column_choice == 1:
        new_value = input("\nEnter the new name: ")
        cur.execute(
            "UPDATE Recipes SET name = %s WHERE id = %s", (new_value, recipe_id)
        )
    elif column_choice == 2:
        new_value = int(input("\nEnter the new cooking time: "))
        cur.execute(
            "UPDATE Recipes SET cooking_time = %s WHERE id = %s", (new_value, recipe_id)
        )
        cur.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        ingredients = cur.fetchall()[0][0].split(", ")
        difficulty = calculate_difficulty(new_value, ingredients)
        cur.execute(
            "UPDATE Recipes SET difficulty = %s WHERE id = %s", (difficulty, recipe_id)
        )
    elif column_choice == 3:
        new_value = input("\nEnter the new ingredient(s): ")
        cur.execute(
            "UPDATE Recipes SET ingredients = %s WHERE id = %s", (new_value, recipe_id)
        )
        cur.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
        cooking_time = cur.fetchall()[0][0]
        difficulty = calculate_difficulty(cooking_time, new_value.split(", "))
        cur.execute(
            "UPDATE Recipes SET difficulty = %s WHERE id = %s", (difficulty, recipe_id)
        )
    conn.commit()
    space()
    print("Recipe updated successfully!")


# Delete a recipe.
def delete_recipe(conn, cur):
    results = cur.execute("SELECT * FROM Recipes")
    results = cur.fetchall()
    space()
    print("Available recipes:")
    for row in results:
        print(f"{row[0]}. {row[1]}")
    while True:
        try:
            recipe_choice = int(
                input("\nEnter the number of the recipe you want to delete: ")
            )
            if recipe_choice not in range(1, len(results) + 1):
                space()
                print("Please select a valid option")
            else:
                break
        except ValueError:
            space()
            print("Please select a valid option")
    recipe_id = results[recipe_choice - 1][0]
    cur.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
    conn.commit()
    space()
    print("Recipe deleted successfully!")


# View all recipes.
def view_recipes(cur):
    cur.execute("SELECT * FROM Recipes")
    results = cur.fetchall()
    if len(results) == 0:
        space()
        print("No recipes found")
    else:
        for row in results:
            space()
            print(f"Name: {row[1]}")
            print(f"Ingredients: {row[2]}")
            print(f"Cooking time: {row[3]} minutes")
            print(f"Difficulty: {row[4]}")


main_menu(conn, cur)
print("Goodbye!")