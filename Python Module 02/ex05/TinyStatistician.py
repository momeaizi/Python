from math import sqrt

class TinyStatistician():
    """"""

    @staticmethod
    def mean(vector):
        """calculate the mean of a given vector.
        Args:
        vector: a vector.
        Return:
        A float.
        None if the vector is empty.
        """

        if len(vector) == 0:
            return None
    
        ans = 0.0
        for x in vector:
            ans += x
        return ans / len(vector)


    @staticmethod
    def median(vector):
        """calculate the median of a given vector.
        Args:
        vector: a vector.
        Return:
        A float.
        None if the vector is empty.
        """

        n = len(vector)

        if len(vector) == 0:
            return None
        
        vector = sorted(vector)

        if n % 2 == 0:
            middle = n // 2
            return (vector[middle - 1] + vector[middle]) / 2
        else:
            return vector[n // 2]
    

    @staticmethod
    def quartiles(vector):
        """calculate the median of a given vector.
        Args:
        vector: a vector.
        Return:
        A float.
        None if the vector is empty.
        """

        n = len(vector)

        if len(vector) == 0:
            return None
        
        vector = sorted(vector)

        if n % 2 == 0:
            first_quartile = (vector[n // 4 - 1] + vector[n // 4]) / 2
            third_quartile = (vector[(n * 3) // 4 - 1] + vector[(n * 3) // 4]) / 2
            return (first_quartile, third_quartile)
        else:
            return (vector[n // 4], vector[(n * 3) // 4])
        


    @staticmethod
    def var(vector):
        """calculate the median of a given vector.
        Args:
        vector: a vector.
        Return:
        A float.
        None if the vector is empty.
        """

        n = len(vector)

        if len(vector) == 0:
            return None

        med = TinyStatistician.median(vector)
        ans = 0.0

        for x in vector:
            ans += (x - med) ** 2

        return ans / n

    @staticmethod
    def std(vector):
        """calculate the median of a given vector.
        Args:
        vector: a vector.
        Return:
        A float.
        None if the vector is empty.
        """

        n = len(vector)

        if len(vector) == 0:
            return None

        return sqrt(TinyStatistician.var(vector))



tinyStatistician = TinyStatistician()
x = [2, 2, 4, 5, 5, 5, 8, 9, 9, 9, 12]
x = [17, 15, 16, 14, 19]



print(tinyStatistician.mean(x))
print(tinyStatistician.median(x))
print(tinyStatistician.quartiles(x))
print(tinyStatistician.var(x))
print(tinyStatistician.std(x))