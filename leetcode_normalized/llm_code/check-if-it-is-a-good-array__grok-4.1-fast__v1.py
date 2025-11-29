import math

class C1:

    def isGoodArray(self, a1):
        return math.gcd(*a1) == 1
