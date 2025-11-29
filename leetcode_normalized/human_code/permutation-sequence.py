import math

class C1(object):

    def getPermutation(self, a1, a2):
        """
        """
        v1, a2, v3 = ('', a2 - 1, math.factorial(a1 - 1))
        v4 = [i for v5 in range(1, a1 + 1)]
        for v5 in reversed(range(a1)):
            v6 = v4[a2 / v3]
            v1 += str(v6)
            v4.remove(v6)
            if v5 > 0:
                a2 %= v3
                v3 /= v5
        return v1
