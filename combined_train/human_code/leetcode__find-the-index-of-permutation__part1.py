class C1(object):

    def getPermutationIndex(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        class BIT(object):

            def __init__(self, a1):
                self.__bit = [0] * (a1 + 1)

            def add(self, a1, a2):
                a1 += 1
                while a1 < len(self.__bit):
                    self.__bit[a1] = (self.__bit[a1] + a2) % v1
                    a1 += a1 & -a1

            def query(self, a1):
                a1 += 1
                v2 = 0
                while a1 > 0:
                    v2 = (v2 + self.__bit[a1]) % v1
                    a1 -= a1 & -a1
                return v2
        v2 = [0] * len(a1)
        v2[0] = 1
        for v3 in range(len(v2) - 1):
            v2[v3 + 1] = (v3 + 1) * v2[v3] % v1
        v4 = 0
        v5 = BIT(len(a1))
        for v3, v6 in enumerate(a1):
            v4 = (v4 + (v6 - 1 - v5.query(v6 - 1 - 1)) % v1 * v2[len(a1) - 1 - v3] % v1) % v1
            v5.add(v6 - 1, +1)
        return v4
