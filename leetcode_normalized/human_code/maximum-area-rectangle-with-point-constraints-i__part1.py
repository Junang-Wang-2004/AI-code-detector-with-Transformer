class C1(object):

    def maxRectangleArea(self, a1):
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
        a1.sort()
        v1 = {y: idx for v2, v3 in enumerate(sorted(set((v3 for v4, v3 in a1))))}
        v5 = BIT(len(v1))
        v6 = {}
        v7 = -1
        for v8, (v9, v3) in enumerate(a1):
            v10 = v1[v3]
            v5.add(v10, +1)
            if not (v8 - 1 >= 0 and a1[v8 - 1][0] == v9):
                continue
            v11 = v1[a1[v8 - 1][1]]
            v12 = v5.query(v10) - v5.query(v11 - 1)
            if (v11, v10) in v6 and v6[v11, v10][0] == v12 - 2:
                v7 = max(v7, (v9 - v6[v11, v10][1]) * (v3 - a1[v8 - 1][1]))
            v6[v11, v10] = (v12, v9)
        return v7
