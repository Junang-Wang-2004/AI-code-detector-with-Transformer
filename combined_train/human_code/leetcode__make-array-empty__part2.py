class C1(object):

    def countOperationsToEmptyArray(self, a1):
        """
        """

        class BIT(object):

            def __init__(self, a1):
                self.__bit = [0] * (a1 + 1)

            def add(self, a1, a2):
                a1 += 1
                while a1 < len(self.__bit):
                    self.__bit[a1] += a2
                    a1 += a1 & -a1

            def query(self, a1):
                a1 += 1
                v2 = 0
                while a1 > 0:
                    v2 += self.__bit[a1]
                    a1 -= a1 & -a1
                return v2
        v1 = BIT(len(a1))
        v2 = list(range(len(a1)))
        v2.sort(key=lambda x: a1[x])
        v3 = len(a1)
        v4 = -1
        for v5 in v2:
            if v4 == -1:
                v3 += v5
            elif v4 < v5:
                v3 += v5 - v4 - (v1.query(v5) - v1.query(v4 - 1))
            else:
                v3 += len(a1) - 1 - v1.query(len(a1) - 1) - (v4 - v5 - (v1.query(v4) - v1.query(v5 - 1)))
            v1.add(v5, 1)
            v4 = v5
        return v3
