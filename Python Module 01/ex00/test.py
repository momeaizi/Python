from book import Book
from recipe import Recipe

def invalidRecipeArgs():
    invalidNameType = Recipe(65, 3, 50, ["olive oil", "Flour", "tomatoes"]\
                            , "dish of Italian", "lunch")
    invalidCooking_lvlType = Recipe("pizza", "3", 50, ["olive oil", "Flour", "tomatoes"]\
                            , "dish of Italian", "lunch")
    invalidCooking_lvlVal = Recipe("pizza", 10, 50, ["olive oil", "Flour", "tomatoes"]\
                            , "dish of Italian", "lunch")
    invalidCooking_timeType = Recipe("pizza", 3, "50", ["olive oil", "Flour", "tomatoes"]\
                            , "dish of Italian", "lunch")
    invalidCooking_timeVal = Recipe("pizza", 3, -50, ["olive oil", "Flour", "tomatoes"]\
                            , "dish of Italian", "lunch")
    invalidIngredientsType = Recipe("pizza", 3, 50, "ingrediants"\
                            , "dish of Italian", "lunch")
    invalidIngredientType = Recipe("pizza", 3, 50, [1, "olive oil", "Flour", "tomatoes"]\
                            , "dish of Italian", "lunch")
    invalidDescriptionType = Recipe("pizza", 3, 50, ["olive oil", "Flour", "tomatoes"]\
                            , 1, "lunch")
    invalidRecipe_typeType = Recipe("pizza", 3, 50, ["olive oil", "Flour", "tomatoes"]\
                            , "dish of Italian", 1)

def testGet_recipe_by_type(cookBook):
    print("get_recipe_by_types")
    print("\tstarters: \n\t\t", end="")
    print(cookBook.get_recipes_by_types("starter"))
    print("\tlunches: \n\t\t", end="")
    print(cookBook.get_recipes_by_types("lunch"))
    print("\tdesserts: \n\t\t", end="")
    print(cookBook.get_recipes_by_types("dessert"), end="\n\n")

def testGet_recipe_by_name(cookBook):
    print("get_recipe_by_name")
    starter1 = cookBook.get_recipe_by_name("starter1")
    print("\n\n")
    pizza = cookBook.get_recipe_by_name("pizza")
    print("\n\n")
    spaghetti = cookBook.get_recipe_by_name("spaghetti")
    print("\n\n")
    dessert2 = cookBook.get_recipe_by_name("dessert2")
    print("\n\n")


def testAddRecipe():
    pizza = Recipe("pizza", 3, 15, ["olive oil", "Flour", "tomatoes"]\
                    , "dish of Italian", "lunch")
    spaghetti = Recipe("spaghetti", 5, 10, ["olive oil", "pasta", "tomatoes"]\
                    , "dish of Italian", "lunch")
    lunch1 = Recipe("lunch1", 3, 15, ["olive oil", "Flour", "tomatoes"]\
                    , "dish of Italian", "lunch")
    lunch2 = Recipe("lunch2", 5, 10, ["olive oil", "pasta", "tomatoes"]\
                    , "dish of Italian", "lunch")
    starter = Recipe("starter", 3, 15, ["olive oil", "Flour", "tomatoes"]\
                    , "dish of Italian", "starter")
    starter1 = Recipe("starter1", 5, 10, ["olive oil", "pasta", "tomatoes"]\
                    , "dish of Italian", "starter")
    starter2 = Recipe("starter2", 5, 10, ["olive oil", "pasta", "tomatoes"]\
                    , "dish of Italian", "starter")
    dessert = Recipe("dessert", 3, 15, ["olive oil", "Flour", "tomatoes"]\
                    , "dish of Italian", "dessert")
    dessert1 = Recipe("dessert1", 5, 10, ["olive oil", "pasta", "tomatoes"]\
                    , "dish of Italian", "dessert")
    dessert2 = Recipe("dessert2", 5, 10, ["olive oil", "pasta", "tomatoes"]\
                    , "dish of Italian", "dessert")

    recipes = [pizza, spaghetti, lunch1, lunch2, starter, starter1, starter2, dessert, dessert1, dessert2]
    cookBook = Book("cookBook")

    print("creation_date: {}".format(cookBook.creation_date), end="\n\n")

    for recipe in recipes:
        cookBook.add_recipe(recipe)

    return cookBook

if __name__ == "__main__":

    # invalidRecipeArgs()
    cookBook = testAddRecipe()
    testGet_recipe_by_type(cookBook)
    testGet_recipe_by_name(cookBook)
    