class ShoppingList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item in self.shopping_list:
            print(f"{item} already in shopping list")
        else:
            self.shopping_list.append(item)

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)

    def view_list(self):
        print(f"{self.list_name}:")
        for item in self.shopping_list:
            print(f"\t{item}")


pet_store_list = ShoppingList("Pet Store Shopping List")
items = ["Dog Food", "Frisbee", "Bowl", "Collars", "Flea Collars"]

for item in items:
    pet_store_list.add_item(item)
print("-" * 30)
pet_store_list.view_list()

pet_store_list.remove_item("Flea Collars")
print("Flea Collars removed from list")
print("-" * 30)

pet_store_list.add_item("Frisbee")
print("-" * 30)

pet_store_list.view_list()
