from Polynome import Polynome
import sys


def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python main.py \"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\"")
            sys.exit(1)
        
        polynome = Polynome(sys.argv[1])

        print("Reduced form:", polynome.get_reduced_form())
        print("Polynomial degree:", polynome.get_degree())
        polynome.solve()
    
    except Exception as e:
        print(e)
        sys.exit(11)


if __name__ == "__main__":
    main()
