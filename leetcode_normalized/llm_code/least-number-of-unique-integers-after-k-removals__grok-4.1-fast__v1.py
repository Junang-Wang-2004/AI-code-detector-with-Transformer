from collections import Counter

class C1:

    def findLeastNumOfUniqueInts(self, a1, a2):
        v1 = sorted(Counter(a1).values())
        v2 = len(v1)
        for v3 in v1:
            if a2 >= v3:
                a2 -= v3
                v2 -= 1
            else:
                break
        return v2
