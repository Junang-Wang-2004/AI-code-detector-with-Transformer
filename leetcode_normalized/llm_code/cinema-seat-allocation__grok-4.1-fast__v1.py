from collections import defaultdict

class C1:

    def maxNumberOfFamilies(self, a1, a2):
        v1 = defaultdict(int)
        for v2, v3 in a2:
            if 2 <= v3 <= 5:
                v1[v2] |= 1
            if 4 <= v3 <= 7:
                v1[v2] |= 2
            if 6 <= v3 <= 9:
                v1[v2] |= 4
        v4 = 2 * a1
        for v5 in v1.values():
            if v5 & 1 == 0 and v5 & 4 == 0:
                continue
            if v5 != 7:
                v4 -= 1
            else:
                v4 -= 2
        return v4
