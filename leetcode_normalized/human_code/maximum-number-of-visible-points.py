import math

class C1(object):

    def visiblePoints(self, a1, a2, a3):
        """
        """
        v1, v2 = ([], 0)
        for v3 in a1:
            if v3 == a3:
                v2 += 1
                continue
            v1.append(math.atan2(v3[1] - a3[1], v3[0] - a3[0]))
        v1.sort()
        v1.extend([x + 2.0 * math.pi for v4 in v1])
        v5 = 2.0 * math.pi * (a2 / 360.0)
        v6 = v7 = 0
        for v8 in range(len(v1)):
            while v1[v8] - v1[v6] > v5:
                v6 += 1
            v7 = max(v7, v8 - v6 + 1)
        return v7 + v2
