class C1(object):

    def latestTimeCatchTheBus(self, a1, a2, a3):
        """
        """
        a1.sort()
        a2.sort()
        v1 = v2 = 0
        for v3 in range(len(a1) - 1):
            while v2 < len(a2) and a2[v2] <= a1[v3]:
                v1 += 1
                v2 += 1
            v1 = max(v1 - a3, 0)
        v2 -= max(v1 - a3, 0)
        v1 = min(v1, a3)
        while v2 < len(a2) and a2[v2] <= a1[-1] and (v1 + 1 <= a3):
            v1 += 1
            v2 += 1
        return a1[-1] if v1 < a3 and (v2 - 1 < 0 or a2[v2 - 1] != a1[-1]) else next((a2[v3] - 1 for v3 in reversed(range(v2)) if v3 - 1 < 0 or a2[v3] - 1 != a2[v3 - 1]))
