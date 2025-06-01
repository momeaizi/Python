from typing import List, Tuple
import re


class Polynome:
    def __init__(self, equation: str):
        self.__reduced_polynomial = {}
        self.__terms = []
        if not self.__is_valid_equation(equation):
            raise Exception("Invalid Equation!")
        self.__extract_monomials()
    


    def __is_valid_equation(self, equation: str) -> bool:
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

            joined_terms = ''.join(terms)
            if joined_terms != side:
                return False  # leftover symbols like '+=' or unmatched operators

            if not terms or not all(monomial_pattern.fullmatch(term) for term in terms):
                return False
            self.__terms.append(terms)
            return True
        
        return is_valid_side(left) and is_valid_side(right)


    def __parse_monomial(self, term: str) -> Tuple[float, int]:
        """
        Parses a monomial term like '5*X^0' or '-9.3*X^2' into a tuple (coefficient, power).
        """
        term = term.replace(" ", "")
        pattern = r'^([+-]?\d+(?:\.\d+)?)\*X\^(\d+)$'
        match = re.fullmatch(pattern, term)

        
        coefficient = float(match.group(1))
        power = int(match.group(2))

        return coefficient, power


    def __extract_monomials(self) -> List[float]:
        for side in range(2):
            # 0 -> left side | 1 -> right side
            for term in self.__terms[side]:
                coefficient, power = self.__parse_monomial(term)
                if side == 1: # if the right side change the sign of the coefficient
                    coefficient *= -1

                if power in self.__reduced_polynomial:
                    self.__reduced_polynomial[power] += coefficient
                else:
                    self.__reduced_polynomial[power] = coefficient
                
                if self.__reduced_polynomial[power] == 0:
                    del self.__reduced_polynomial[power]



    def __calculate_discriminant(self, a: float, b: float, c: float) -> float:
        return b ** 2 - 4 * a * c


    def solve(self):
        degree = self.get_degree()

        if degree > 2:
            raise Exception("The polynomial degree is strictly greater than 2, I can't solve.")


        if degree == 0:
            b = self.__reduced_polynomial.get(0, 0)
            if b == 0:
                print("All real numbers are solutions.")
            else:
                print("No solution, the equation is inconsistent.")
            return
            

        if degree == 1:
            a = self.__reduced_polynomial.get(1, 0)
            b = self.__reduced_polynomial.get(0, 0)
            print("The solution is:")
            print(round(-b / a, 2))
            return

        a = self.__reduced_polynomial.get(2, 0)
        b = self.__reduced_polynomial.get(1, 0)
        c = self.__reduced_polynomial.get(0, 0)

        discriminant = self.__calculate_discriminant(a, b, c)

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
        for power, coef in self.__reduced_polynomial.items():
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
        if not self.__reduced_polynomial:
            return 0
        return max(self.__reduced_polynomial)

