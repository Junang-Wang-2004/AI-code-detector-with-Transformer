class C1:

    def lengthOfLongestSubstringTwoDistinct(self, a1):
        v1 = {}
        v2 = 0
        v3 = 0
        v4 = 0
        for v5 in range(len(a1)):
            v6 = a1[v5]
            if v1.get(v6, 0) == 0:
                v4 += 1
            v1[v6] = v1.get(v6, 0) + 1
            while v4 > 2:
                v7 = a1[v2]
                v1[v7] -= 1
                if v1[v7] == 0:
                    del v1[v7]
                    v4 -= 1
                v2 += 1
            v3 = max(v3, v5 - v2 + 1)
        return v3
