sandwich = {
    "ingredients": [
                    "ham",
                    "bread",
                    "cheese",
                    "tomatoes"
                ],
    "meal":         "lunch",
    "prep_time":    10
}

cake = {
    "ingredients": [
                    "flour",
                    "sugar",
                    "eggs"
                ],
    "meal":         "dessert",
    "prep_time":    60
}

salad = {
    "ingredients": [
                    "avocado",
                    "arugula",
                    "tomatoes",
                    "spinach"
                ],
    "meal":         "lunch",
    "prep_time":    15
}

cookbook = {
    "sandwich": sandwich,
    "cake":     cake,
    "salad":    salad
}


def recipes(recipes):

    for e in recipes:
        print(e)


def recipe_details(recipe_name):
    if recipe_name not in cookbook:
        print("there's no recipe with this name in this cookbook!")
        return
    recipe = cookbook[recipe_name]
    print(f"Recipe for {recipe_name}:")
    print(f"\tIngredients list: {recipe['ingredients']}")
    print(f"\tTo be eaten for {recipe['meal']}.")
    print(f"\tTakes {recipe['prep_time']} minutes of cooking.")


def delete_recipe(recipe_name):
    if recipe_name not in cookbook:
        print("there's no recipe with this name in this cookbook!")
        return
    del cookbook[recipe_name]


def add_recipe(recipe_name):
    if recipe_name not in cookbook:
        print("there's no recipe with this name in this cookbook!")
        return
    del cookbook[recipe_name]


recipe_details("cake")
delete_recipe("cake")
recipe_details("cake")
