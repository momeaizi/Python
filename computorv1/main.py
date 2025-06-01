from typing import List, Tuple
import re
import sys


class Polynome:
    def __init__(self, equation: str):
        self.reduced_polynomial = {}
        self.terms = []
        if not self.is_valid_equation(equation):
            raise Exception("Invalid Equation!")
        self.extract_monomials()
    


    def is_valid_equation(self, equation: str) -> bool:
        equation = equation.replace(" ", "")
        
        # Must contain exactly one '='
        if equation.count('=') != 1:
            return False
        
        left, right = equation.split('=')

        # Helper regex to validate a monomial: a * X^p
        monomial_pattern = re.compile(r'^[+-]?\d+(?:\.\d+)?\*X\^\d+$')

        def is_valid_side(side: str) -> bool:
            # Ensure first term has explicit sign
            if side and side[0] not in '+-':
                side = '+' + side
            # Split terms by + or -
            terms = re.findall(r'[+-][^+-]+', side)
            if not terms or not all(monomial_pattern.fullmatch(term) for term in terms):
                return False
            self.terms.append(terms)
            return True
        
        return is_valid_side(left) and is_valid_side(right)


    def parse_monomial(self, term: str) -> Tuple[float, int]:
        """
        Parses a monomial term like '5*X^0' or '-9.3*X^2' into a tuple (coefficient, power).
        """
        term = term.replace(" ", "")
        pattern = r'^([+-]?\d+(?:\.\d+)?)\*X\^(\d+)$'
        match = re.fullmatch(pattern, term)
        
        if not match:
            raise ValueError(f"Invalid monomial format: '{term}'")
        
        coefficient = float(match.group(1))
        power = int(match.group(2))

        return coefficient, power


    def extract_monomials(self) -> List[float]:
        try:
            for side in range(2):
                for term in self.terms[side]:
                    coefficient, power = self.parse_monomial(term)
                    if side == 1: # if the right side change the sign of the coefficient
                        coefficient *= -1

                    if power in self.reduced_polynomial:
                        self.reduced_polynomial[power] += coefficient
                    else:
                        self.reduced_polynomial[power] = coefficient
                    
                    if self.reduced_polynomial[power] == 0:
                        del self.reduced_polynomial[power]
        except Exception as e:
            print(e)
            sys.exit(1)

    def calculate_discriminant(self, a: float, b: float, c: float) -> float:
        return b ** 2 - 4 * a * c


    def solve(self):

        degree = self.get_degree()

        if degree > 2:
            raise Exception("The polynomial degree is strictly greater than 2, I can't solve.")


        if degree == 0:
            b = self.reduced_polynomial.get(0, 0)
            if b == 0:
                print("All real numbers are solutions.")
            else:
                print("No solution, the equation is inconsistent.")
            return
            

        if degree == 1:
            a = self.reduced_polynomial.get(1, 0)
            b = self.reduced_polynomial.get(0, 0)
            print("The solution is:")
            print(round(-b / a, 2))
            return

        a = self.reduced_polynomial.get(2, 0)
        b = self.reduced_polynomial.get(1, 0)
        c = self.reduced_polynomial.get(0, 0)

        discriminant = self.calculate_discriminant(a, b, c)

        if discriminant < 0:
            print("Discriminant is strictly negative, the two solutions are:")
            print(f"{round(-b / (2 * a), 2)} + {round(((-discriminant) ** 0.5) / (2 * a), 2)} * i")
            print(f"{round(-b / (2 * a), 2)} - {round(((-discriminant) ** 0.5) / (2 * a), 2)} * i")
        elif discriminant == 0:
            print("The solution is:")
            print(-b / (2 * a))
        else:
            print("Discriminant is strictly positive, the two solutions are:")
            print(round((-b - discriminant ** 0.5) / (2 * a), 2))
            print(round((-b + discriminant ** 0.5) / (2 * a), 2))



    def get_reduced_form(self):
        reduced_form = ""
        for power, coef in self.reduced_polynomial.items():
            if coef < 0:
                reduced_form += f" - {-coef} * X^{power}"
            else:
                if reduced_form:
                    reduced_form += " + "
                reduced_form += f"{coef} * X^{power}"
        
        if not reduced_form:
            reduced_form = "0 * X^0"

        return reduced_form + " = 0"

    def get_degree(self):
        if not self.reduced_polynomial:
            return 0
        return max(self.reduced_polynomial)



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
