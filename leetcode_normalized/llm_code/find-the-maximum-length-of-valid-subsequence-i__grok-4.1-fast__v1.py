class C1:

    def maximumLength(self, a1):
        v1 = v2 = v3 = 0
        v4 = -1
        for v5 in a1:
            v6 = v5 % 2
            if v6 == 0:
                v1 += 1
            else:
                v2 += 1
            if v6 != v4:
                v3 += 1
                v4 = v6
        return max(v1, v2, v3)
