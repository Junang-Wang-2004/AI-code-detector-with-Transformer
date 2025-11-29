class C1(object):

    def lengthOfLongestSubstringKDistinct(self, a1, a2):
        """
        """
        v1, v2, v3, v4 = (0, 0, 0, [0 for v5 in range(256)])
        for v6, v7 in enumerate(a1):
            if v4[ord(v7)] == 0:
                v3 += 1
            v4[ord(v7)] += 1
            while v3 > a2:
                v4[ord(a1[v2])] -= 1
                if v4[ord(a1[v2])] == 0:
                    v3 -= 1
                v2 += 1
            v1 = max(v1, v6 - v2 + 1)
        return v1
