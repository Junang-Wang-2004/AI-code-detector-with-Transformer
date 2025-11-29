class C1:

    def longestAlternatingSubarray(self, a1, a2):
        v1 = 0
        v2 = 0
        v3 = 0
        for v4 in a1:
            v5 = v4 % 2
            if v4 > a2:
                v2 = 0
            elif v2 == 0:
                if v5 == 0:
                    v2 = 1
                    v3 = 1
            elif v5 == v3:
                v2 += 1
                v3 = 1 - v3
            elif v5 == 0:
                v2 = 1
                v3 = 1
            else:
                v2 = 0
            v1 = max(v1, v2)
        return v1
