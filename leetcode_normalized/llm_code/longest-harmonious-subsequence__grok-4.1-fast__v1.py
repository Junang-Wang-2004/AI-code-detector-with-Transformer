from collections import Counter

class C1:

    def findLHS(self, a1):
        v1 = Counter(a1)
        v2 = 0
        for v3 in v1:
            v4 = v3 + 1
            if v4 in v1:
                v2 = max(v2, v1[v3] + v1[v4])
        return v2
