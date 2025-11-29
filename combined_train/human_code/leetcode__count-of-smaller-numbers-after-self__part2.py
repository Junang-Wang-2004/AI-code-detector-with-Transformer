class C1(object):

    def countSmaller(self, a1):
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
        v1 = sorted(zip(a1, list(range(len(a1)))))
        v2 = {i: new_i for v3, (v4, v5) in enumerate(v1)}
        v6, v7 = ([0] * len(a1), BIT(len(a1)))
        for v5 in reversed(range(len(a1))):
            v6[v5] = v7.query(v2[v5] - 1)
            v7.add(v2[v5], 1)
        return v6
