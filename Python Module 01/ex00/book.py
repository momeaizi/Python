from datetime import datetime
from recipe import Recipe

class Book():
    def __init__(self, bookName):
        self.name = bookName
        self.creation_date = datetime.now()
        self.last_update = datetime.now()
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": [],
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    print(recipe)
                    return recipe

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        if recipe_type not in ["starter", "lunch", "dessert"]:
            print("recipe_type must be one of these (starter, lunch, dessert)!")
            exit(1)
        return [
            recipe.name
            for recipe in self.recipes_list[recipe_type]
        ]

    def add_recipe(self, recipe):
        """Add arecipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("you must provide a recipe object!")
            exit(1)
        self.last_update = datetime.now()
        self.recipes_list[recipe.recipe_type].append(recipe)
