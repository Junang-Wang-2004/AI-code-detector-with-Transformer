import math

class C1(object):

    def numPoints(self, a1, a2):
        """
        """

        def count_points(a1, a2, a3):
            v1 = []
            for v2 in range(len(a1)):
                if a3 == v2:
                    continue
                v3, v4 = (a1[a3][0] - a1[v2][0], a1[a3][1] - a1[v2][1])
                v5 = math.sqrt(v3 ** 2 + v4 ** 2)
                if v5 > 2 * a2:
                    continue
                v6, v7 = (math.acos(v5 / (2 * a2)), math.atan2(v4, v3))
                (v1.append((v7 - v6, 0)), v1.append((v7 + v6, 1)))
            v1.sort()
            v8, v9 = (1, 1)
            for v10, v11 in v1:
                if not v11:
                    v9 += 1
                else:
                    v9 -= 1
                v8 = max(v8, v9)
            return v8
        return max((count_points(a1, a2, i) for v1 in range(len(a1))))
