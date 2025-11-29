class C1:

    def lengthOfLongestSubstringKDistinct(self, a1, a2):
        v1 = {}
        v2 = 0
        v3 = 0
        for v4 in range(len(a1)):
            v5 = a1[v4]
            v1[v5] = v1.get(v5, 0) + 1
            while len(v1) > a2:
                v6 = a1[v2]
                v1[v6] -= 1
                if v1[v6] == 0:
                    del v1[v6]
                v2 += 1
            v3 = max(v3, v4 - v2 + 1)
        return v3
