
def validArg(arg, argName, expectedType):
    valid = "if not isinstance(arg, {0}):\
        \n\tprint(\"{1} must be of type {0} not {2}!\")\
        \n\texit(1)".format(expectedType, argName, type(arg))
    
    exec(valid)

    if argName != "description" and expectedType == "str" and len(arg) == 0:
        print("{} must not be emty!".format(argName))
        exit(1)

    if argName == "recipe_type" and arg not in ["starter", "lunch", "dessert"]:
        print("recipe_type must be one of these (starter, lunch, dessert)")
        exit(1)

    if argName == "cooking_lvl" and not 1 <= arg <= 5:
        print("cooking_lvl must be between [1, 5]!")
        exit(1)
    if argName == "cooking_time" and arg < 0:
        print("cooking_time must be positive!")
        exit(1)

class Recipe():

    """Recipe class"""

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        valid = True

        validArg(name, "name", "str")
        self.name = name
        validArg(cooking_lvl, "cooking_lvl", "int")
        self.cooking_lvl = cooking_lvl
        validArg(cooking_time, "cooking_time", "int")
        self.cooking_time = cooking_time
        validArg(ingredients, "ingredients", "list")
        for ingr in ingredients:
            validArg(ingr, "ingredients", "str")
        self.ingredients = ingredients
        validArg(description, "description", "str")
        self.description = description
        validArg(recipe_type, "recipe_type", "str")
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        return """\
name: {}
cooking level: {}
cooking time: {} min
ingredients: {}
description: {}
type: {}""".format(self.name, self.cooking_lvl, self.cooking_time, ', '.join(self.ingredients), self.description, self.recipe_type)
