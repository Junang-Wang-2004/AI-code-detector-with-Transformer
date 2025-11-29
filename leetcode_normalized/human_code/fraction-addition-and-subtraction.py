import re

class C1(object):

    def fractionAddition(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = list(map(int, re.findall('[+-]?\\d+', a1)))
        v2, v3 = (0, 1)
        for v4 in range(0, len(v1), 2):
            v5, v6 = (v1[v4], v1[v4 + 1])
            v2 = v2 * v6 + v5 * v3
            v3 *= v6
            v7 = gcd(v2, v3)
            v2 //= v7
            v3 //= v7
        return '%d/%d' % (v2, v3)
