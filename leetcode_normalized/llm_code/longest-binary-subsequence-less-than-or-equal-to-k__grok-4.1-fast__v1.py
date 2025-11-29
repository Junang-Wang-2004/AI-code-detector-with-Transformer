class C1:

    def longestSubsequence(self, a1, a2):
        v1 = a1[::-1]
        v2 = 0
        v3 = 1
        v4 = a2
        for v5 in v1:
            if v5 == '0':
                v2 += 1
            elif v3 <= v4:
                v4 -= v3
                v2 += 1
            if v3 <= v4:
                v3 *= 2
        return v2
