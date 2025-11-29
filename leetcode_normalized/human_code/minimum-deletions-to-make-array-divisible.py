from functools import reduce

class C1(object):

    def minOperations(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = reduce(gcd, a2)
        v2 = float('inf')
        for v3 in a1:
            if v1 % v3 == 0:
                v2 = min(v2, v3)
        return sum((v3 < v2 for v3 in a1)) if v2 != float('inf') else -1
