import sys


def parity(nbr: int):
    if nbr == 0:
        print("I'm Zero.")
    elif nbr % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")


n = len(sys.argv)
if n > 2:
    print("AssertionError: more than one argument are provided")
elif n == 2:
    try:
        nbr = int(sys.argv[1])
        parity(nbr)
    except ValueError:
        print("AssertionError: argument is not an integer")
