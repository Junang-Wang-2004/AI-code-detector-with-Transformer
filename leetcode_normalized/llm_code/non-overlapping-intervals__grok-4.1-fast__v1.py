class C1:

    def eraseOverlapIntervals(self, a1):
        v1 = sorted(a1, key=lambda x: x[1])
        v2 = 0
        v3 = float('-inf')
        for v4, v5 in v1:
            if v4 >= v3:
                v2 += 1
                v3 = v5
        return len(a1) - v2
