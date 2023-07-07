from random import shuffle

def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded."""

    if type(text) != str:
        print("text must be of type str!")
        return
    if type(sep) != str:
        print("separator must be of type str!")
        return
    
    tokens = text.split(sep) # split the text

    if option != None:
        # option validation
        if type(option) != str:
            print("option must be of type str!")
            return
        if option not in ["shuffle", "unique", "ordered"]:
            print("invalid option! available options (\"shuffle\", \"unique\", \"ordered\")")
            return
        
        #
        if option == "shuffle":
            shuffle(tokens)
        elif option == "unique":
            tokens = list(set(tokens))
        elif option == "ordered":
            tokens = sorted(tokens)


    for token in tokens:
        yield token

