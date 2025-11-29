import math

class C1(object):

    def findTheArrayConcVal(self, a1):
        """
        """
        return sum((a1[i] * 10 ** (int(math.log10(a1[~i])) + 1) for v1 in range(len(a1) // 2))) + sum((a1[v1] for v1 in range(len(a1) // 2, len(a1))))
