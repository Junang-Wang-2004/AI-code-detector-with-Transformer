class C1:

    def maximumScore(self, a1, a2):
        v1 = len(a1)
        v2 = a1[a2]
        v3 = a1[a2]
        v4, v5 = (a2, a2)
        while v4 > 0 or v5 < v1 - 1:
            if v4 == 0:
                v5 += 1
                v3 = min(v3, a1[v5])
            elif v5 == v1 - 1:
                v4 -= 1
                v3 = min(v3, a1[v4])
            elif a1[v4 - 1] >= a1[v5 + 1]:
                v4 -= 1
                v3 = min(v3, a1[v4])
            else:
                v5 += 1
                v3 = min(v3, a1[v5])
            v2 = max(v2, v3 * (v5 - v4 + 1))
        return v2
