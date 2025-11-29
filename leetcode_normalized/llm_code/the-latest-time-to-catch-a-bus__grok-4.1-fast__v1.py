class C1(object):

    def latestTimeCatchTheBus(self, a1, a2, a3):
        a1.sort()
        a2.sort()
        v1 = 0
        v2 = 0
        for v3 in a1[:-1]:
            while v2 < len(a2) and a2[v2] <= v3:
                v1 += 1
                v2 += 1
            v1 = max(0, v1 - a3)
        v4 = max(0, v1 - a3)
        v2 -= v4
        v5 = min(v1, a3)
        v6 = a1[-1]
        while v2 < len(a2) and a2[v2] <= v6 and (v5 < a3):
            v5 += 1
            v2 += 1
        if v5 < a3 and (v2 == 0 or a2[v2 - 1] != v6):
            return v6
        for v7 in range(v2 - 1, -1, -1):
            if v7 == 0 or a2[v7] != a2[v7 - 1] + 1:
                return a2[v7] - 1
