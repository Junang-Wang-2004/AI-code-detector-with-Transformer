class C1(object):

    def getPermutationIndex(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [1] * 2

        def factorial(a1):
            while len(v2) <= a1:
                v2.append(v2[-1] * len(v2) % v1)
            return v2[a1]

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
        v3 = 0
        v4 = BIT(len(a1))
        for v5, v6 in enumerate(a1):
            v3 = (v3 + (v6 - 1 - v4.query(v6 - 1 - 1)) % v1 * factorial(len(a1) - 1 - v5) % v1) % v1
            v4.add(v6 - 1, +1)
        return v3
