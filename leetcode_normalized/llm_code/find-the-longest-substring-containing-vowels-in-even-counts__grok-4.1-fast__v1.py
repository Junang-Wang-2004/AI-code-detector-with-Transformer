class C1:

    def findTheLongestSubstring(self, a1):
        v1 = 'aeiou'
        v2 = {0: -1}
        v3 = 0
        v4 = 0
        for v5, v6 in enumerate(a1):
            if v6 in v1:
                v7 = v1.index(v6)
                v3 ^= 1 << v7
            if v3 in v2:
                v4 = max(v4, v5 - v2[v3])
            else:
                v2[v3] = v5
        return v4
