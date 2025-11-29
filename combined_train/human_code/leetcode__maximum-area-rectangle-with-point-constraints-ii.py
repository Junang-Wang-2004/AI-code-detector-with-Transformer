class C1(object):

    def maxRectangleArea(self, a1, a2):
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
        v1 = sorted(((a1[i], a2[i]) for v2 in range(len(a1))))
        v3 = {y: idx for v4, v5 in enumerate(sorted(set(a2)))}
        v6 = BIT(len(v3))
        v7 = {}
        v8 = -1
        for v2, (v9, v5) in enumerate(v1):
            v10 = v3[v5]
            v6.add(v10, +1)
            if not (v2 - 1 >= 0 and v1[v2 - 1][0] == v9):
                continue
            v11 = v3[v1[v2 - 1][1]]
            v12 = v6.query(v10) - v6.query(v11 - 1)
            if (v11, v10) in v7 and v7[v11, v10][0] == v12 - 2:
                v8 = max(v8, (v9 - v7[v11, v10][1]) * (v5 - v1[v2 - 1][1]))
            v7[v11, v10] = (v12, v9)
        return v8
