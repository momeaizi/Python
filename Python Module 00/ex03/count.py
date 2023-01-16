import sys
import string


def text_analyzer(s=None):

    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if not isinstance(s, str):
        print("AssertionError: argument is not a string")
        return
    if (s is None):
        s = input("What is the text to analyze?\n>> ")
    punc = 0
    upper = 0
    lower = 0
    spaces = 0
    for c in s:
        if c in string.punctuation:
            punc += 1
        elif c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isspace():
            spaces += 1
    print("The text contains 8 character(s):")
    print("- " + str(upper) + "\tupper letter(s)")
    print("- " + str(lower) + "\tlower letter(s)")
    print("- " + str(punc) + "\tpunctuation mark(s)")
    print("- " + str(spaces) + "\tspace(s)")


if __name__ == "__main__":

    n = len(sys.argv)
    if n > 2:
        print("AssertionError: more than one argument are provided")
    elif n == 2:
        text_analyzer(sys.argv[1])
