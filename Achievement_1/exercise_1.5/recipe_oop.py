class Recipe:
    all_ingredients = (
        []
    )  # Class variable to keep track of all ingredients across recipes

    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def add_ingredients(self, *ingredients):
        for i in ingredients:
            self.ingredients.append(i)
        self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    def __str__(self):
        return (
            f"Recipe: {self.name}\n"
            f"Ingredients: {', '.join(self.ingredients)}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.get_difficulty()}"
        )

    # search for recipes based on ingredients
    def recipe_search(self, data, search_term):
        print(f"Recipes containing '{search_term}':")
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)


# Main Code


# separators for readability
def space():
    print("-" * 35)


for i in range(2):
    space()

# creating objects under Recipe class
tea = Recipe("tea", 5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
print(tea)
space()

coffee = Recipe("coffee", 5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
print(coffee)
space()

cake = Recipe("cake", 5)
cake.add_ingredients(
    "Butter", "Sugar", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"
)
print(cake)
space()

banana_smoothie = Recipe("banana_smoothie", 5)
banana_smoothie.add_ingredients(
    "Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"
)
print(banana_smoothie)
for i in range(2):
    space()

# wrap recipes in list
recipes_list = [tea, coffee, cake, banana_smoothie]

ingredients_to_search = ["Water", "Sugar", "Bananas"]

for ingredient in ingredients_to_search:
    print(f"Recipes containing '{ingredient}':")
    for recipe in recipes_list:
        if recipe.search_ingredient(ingredient):
            print(recipe)
            space()
    space()
