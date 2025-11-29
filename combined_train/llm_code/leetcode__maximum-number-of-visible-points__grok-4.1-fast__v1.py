import math

class C1:

    def visiblePoints(self, a1, a2, a3):
        v1 = []
        v2 = 0
        v3, v4 = a3
        for v5, v6 in a1:
            if v5 == v3 and v6 == v4:
                v2 += 1
                continue
            v7 = v5 - v3
            v8 = v6 - v4
            v1.append(math.atan2(v8, v7))
        v1.sort()
        v9 = v1 + [theta + 2 * math.pi for v10 in v1]
        v11 = math.radians(a2)
        v12 = 0
        v13 = 0
        for v14 in range(len(v9)):
            while v9[v14] - v9[v13] > v11:
                v13 += 1
            v12 = max(v12, v14 - v13 + 1)
        return v12 + v2
