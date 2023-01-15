import sys


def operations(a: int, b: int):
    print("Sum:\t\t" + str(a + b))
    print("Difference:\t" + str(a - b))
    print("Product:\t" + str(a * b))
    print("Quotient:\t" + (str(a / b) if b != 0 else "ERROR (division by zero)"))
    print("Remainder:\t" + (str(a % b) if b != 0 else "ERROR (modulo by zero)"))

if __name__ == "__main__":
    n = len(sys.argv)
    if n < 3:
        print("Usage: python operations.py <number1> <number2>")
    elif n > 3:
        print("AssertionError: too many arguments")
    else:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            operations(a, b)
        except ValueError:
            print("AssertionError: only integers")