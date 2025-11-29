from collections import Counter

class C1:

    def findPairs(self, a1, a2):
        if a2 < 0:
            return 0
        v1 = Counter(a1)
        v2 = 0
        if a2 == 0:
            for v3 in v1.values():
                if v3 > 1:
                    v2 += 1
        else:
            for v4 in v1:
                if v4 + a2 in v1:
                    v2 += 1
        return v2
