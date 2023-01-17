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


def recipes():

    for e in cookbook:
        print(e)


def recipe_details():
    name = input("Please enter a recipe name to get its details:\n>> ")
    if name not in cookbook:
        print("there's no recipe with this name in this cookbook!")
        return
    recipe = cookbook[name]
    print(f"Recipe for {name}:")
    print(f"\tIngredients list: {recipe['ingredients']}")
    print(f"\tTo be eaten for {recipe['meal']}.")
    print(f"\tTakes {recipe['prep_time']} minutes of cooking.")


def delete_recipe():
    name = input(">>> Enter the recipe name:\n")
    if name not in cookbook:
        print("there's no recipe with this name in this cookbook!")
        return
    del cookbook[name]


def add_recipe():
    recipe = {}
    name = input(">>> Enter a name:\n")
    if name in cookbook:
        print(f"{name} is already in the cookbook!")
        return
    recipe['ingredients'] = list()
    print(">>> Enter ingredients:")
    while True:
        ingredient = input()
        if len(ingredient) is 0:
            break
        recipe['ingredients'].append(ingredient)
    recipe['meal'] = input(">>> Enter a meal type:\n")
    prep_time = input(">>> Enter a preparation time:\n")
    if prep_time.isnumeric():
        recipe['prep_time'] = int(prep_time)
    else:
        print("invalid value!")
        return
    cookbook[name] = recipe


def prompt():

    list_options()
    while True:
        option = input("\nPlease select an option:\n>> ")
        if option == "1":
            add_recipe()
        elif option == "2":
            delete_recipe()
        elif option == "3":
            recipe_details()
        elif option == "4":
            recipes()
        elif option == "5":
            print("\nCookbook closed. Goodbye !")
            exit(0)
        else:
            print("Sorry, this option does not exist.")
            list_options()


def list_options():

    print("List of available option:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit")


if __name__ == "__main__":
    print("Welcome to the Python Cookbook !")
    prompt()
