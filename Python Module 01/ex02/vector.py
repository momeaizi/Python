

class Vector():
    """A Simple Vector Class"""

    def __init__(self, arg):

        if type(arg) == type(int):
            n = arg
            if n < 0:
                print("size cannot be negative!")
                self.values = [[]]
                self.shape = (0, 0)
            else:
                self.values = [[float(i)] for i in range(n)]
                self.shape = (1, n)

        elif type(arg) == type(tuple):
            span = arg
            if span[0] > span[1]:
                print("Range error!")
                self.values = [[]]
                self.shape = (0, 0)
            else:
                self.values = [[float(i)] for i in range(span[0], span[1])]
                self.shape = (1, span[1] - span[0])
        else:
            self.values = arg
            
            if len(self.values) > 1:
                self.shape = (len(self.values), 1)
            else:
                self.shape = (1, len(self.values[0]))
            

    def dot(self, other: 'Vector') -> float:
        """return the dot product of two vectors"""

        ans = float(0)
        if self.shape[0] == 1:
            for x, y in zip(self.values[0], other.values[0]):
                ans += (x * y)
        else:
            for x, y in zip(self.values, other.values):
                ans += (x[0] * y[0])
        return ans
    
    def T(self) -> 'Vector':
        """return the transpose of the vector"""

        if self.shape[0] == 1:
            return Vector([[x] for x in self.values[0]])
        else:
            return Vector([[x[0] for x in self.values]])
        
    def __add__(self, other: 'Vector'):
        if self.shape == other.shape:
            if self.shape[0] == 1:
                return Vector([[x + y for x, y in zip(self.values[0], other.values[0])]])
            else:
                return Vector([[x[0] + y[0]] for x, y in zip(self.values, other.values)])

    def __radd__(self, other: 'Vector'):
        if self.shape == other.shape:
            if self.shape[0] == 1:
                return Vector([[x + y for x, y in zip(self.values[0], other.values[0])]])
            else:
                return Vector([[x[0] + y[0]] for x, y in zip(self.values, other.values)])

    def __sub__(self, other: 'Vector'):
        if self.shape == other.shape:
            if self.shape[0] == 1:
                return Vector([[x - y for x, y in zip(self.values[0], other.values[0])]])
            else:
                return Vector([[x[0] - y[0]] for x, y in zip(self.values, other.values)])

    def __sub__(self, other: 'Vector'):
        if self.shape == other.shape:
            if self.shape[0] == 1:
                return Vector([[y - x for x, y in zip(self.values[0], other.values[0])]])
            else:
                return Vector([[y[0] - x[0]] for x, y in zip(self.values, other.values)])

    def __truediv__(self, scalar: float):
        if scalar == 0.:
            ZeroDivisionError("division by zero.")
        return Vector([x / scalar for r in self.values for x in r])
    
    def __rtruediv__(self, scalar: float):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __mul__(self, scalar: float):
        return Vector([x * scalar for r in self.values for x in r])

    def __rmul__(self, scalar: float):
        return Vector([x * scalar for r in self.values for x in r])

    def __str__(self):
        return "Vector({})".format(self.values)

    def __repr__(self):
        return str(self.values)


