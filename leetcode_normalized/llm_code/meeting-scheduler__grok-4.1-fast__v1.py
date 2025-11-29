class C1:

    def minAvailableDuration(self, a1, a2, a3):
        v1 = sorted(a1)
        v2 = sorted(a2)
        v3, v4 = (0, 0)
        while v3 < len(v1) and v4 < len(v2):
            v5 = max(v1[v3][0], v2[v4][0])
            v6 = min(v1[v3][1], v2[v4][1])
            if v6 - v5 >= a3:
                return [v5, v5 + a3]
            if v1[v3][1] <= v2[v4][1]:
                v3 += 1
            else:
                v4 += 1
        return []
