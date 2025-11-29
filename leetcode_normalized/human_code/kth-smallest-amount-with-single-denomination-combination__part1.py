import itertools
from functools import reduce

class C1(object):

    def findKthSmallest(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def lcm(a1, a2):
            return a1 // gcd(a1, a2) * a2

        def check(a1):
            return sum(((-1 if i + 1 & 1 else +1) * (a1 // l) for v1 in range(1, len(a1) + 1) for v2 in lookup[v1])) >= a2

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3 in range(1, len(a1) + 1):
            for v4 in itertools.combinations(a1, v3):
                v1[v3].append(reduce(lcm, v4))
        v5 = min(a1)
        v6 = 1
        for v3 in range(1, 25 + 1):
            v6 = lcm(v6, v3)
        return binary_search(v5, a2 * v5, check)
