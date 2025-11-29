class C1:

    def maxCount(self, a1, a2, a3):
        v1 = set(a1)
        v2 = 0
        v3 = 0
        v4 = 1
        while v4 <= a2:
            if v4 in v1:
                v4 += 1
                continue
            if v3 + v4 > a3:
                break
            v3 += v4
            v2 += 1
            v4 += 1
        return v2
