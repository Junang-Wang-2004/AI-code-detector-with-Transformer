class C1:

    def findRadius(self, a1, a2):
        a1.sort()
        a2.sort()
        v1 = 0
        v2 = 0
        v3 = len(a2)
        for v4 in a1:
            while v2 < v3 and a2[v2] < v4:
                v2 += 1
            v5 = float('inf') if v2 == v3 else a2[v2] - v4
            v6 = float('inf') if v2 == 0 else v4 - a2[v2 - 1]
            v7 = min(v5, v6)
            v1 = max(v1, v7)
        return v1
