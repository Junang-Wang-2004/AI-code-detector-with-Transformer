import itertools

class C1(object):

    def sumFourDivisors(self, a1):
        """
        """

        def factorize(a1):
            v1 = []
            v2 = 2
            while v2 * v2 <= a1:
                v3 = 0
                while a1 % v2 == 0:
                    a1 //= v2
                    v3 += 1
                if v3:
                    v1.append([v2, v3])
                v2 += 1 if v2 == 2 else 2
            if a1 > 1:
                v1.append([a1, 1])
            return v1
        v1 = 0
        for v2 in map(factorize, a1):
            if len(v2) == 1 and v2[0][1] == 3:
                v3 = v2[0][0]
                v1 += (v3 ** 4 - 1) // (v3 - 1)
            elif len(v2) == 2 and v2[0][1] == v2[1][1] == 1:
                v3, v4 = (v2[0][0], v2[1][0])
                v1 += (1 + v3) * (1 + v4)
        return v1
