class C1:

    def minIncrementForUnique(self, a1):
        a1.sort()
        v1 = 0
        v2 = a1[0]
        for v3 in a1[1:]:
            v4 = v2 + 1
            if v3 < v4:
                v1 += v4 - v3
                v2 = v4
            else:
                v2 = v3
        return v1
