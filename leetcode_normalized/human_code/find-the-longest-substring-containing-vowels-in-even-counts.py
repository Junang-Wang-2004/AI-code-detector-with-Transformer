class C1(object):

    def findTheLongestSubstring(self, a1):
        """
        """
        v1 = 'aeiou'
        v2, v3, v4 = (0, 0, [-2] * 2 ** len(v1))
        v4[0] = -1
        for v5, v6 in enumerate(a1):
            v7 = v1.find(v6)
            v3 ^= 1 << v7 if v7 >= 0 else 0
            if v4[v3] == -2:
                v4[v3] = v5
            v2 = max(v2, v5 - v4[v3])
        return v2
