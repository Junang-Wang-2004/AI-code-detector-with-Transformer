import math

class C1(object):

    def numPoints(self, a1, a2):
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1):
            v4 = 1
            v5 = []
            for v6 in range(v1):
                if v3 == v6:
                    continue
                v7 = a1[v3][0] - a1[v6][0]
                v8 = a1[v3][1] - a1[v6][1]
                v9 = v7 * v7 + v8 * v8
                if v9 == 0:
                    v4 += 1
                    continue
                if v9 > 4 * a2 * a2:
                    continue
                v10 = math.sqrt(v9)
                v11 = math.atan2(v8, v7)
                v12 = math.acos(v10 / (2 * a2))
                v5.append((v11 - v12, False))
                v5.append((v11 + v12, True))
            v5.sort(key=lambda e: (e[0], e[1]))
            v13 = v4
            v14 = v4
            for v15, v16 in v5:
                if v16:
                    v13 -= 1
                else:
                    v13 += 1
                v14 = max(v14, v13)
            v2 = max(v2, v14)
        return v2
