class C1(object):

    def longestAwesome(self, a1):
        """
        """
        v1 = 10
        v2, v3, v4 = (0, 0, [len(a1)] * 2 ** v1)
        v4[0] = -1
        for v5, v6 in enumerate(a1):
            v3 ^= 2 ** (ord(v6) - ord('0'))
            if v4[v3] == len(a1):
                v4[v3] = v5
            v2 = max(v2, v5 - v4[v3])
            for v7 in range(v1):
                v2 = max(v2, v5 - v4[v3 ^ 2 ** v7])
        return v2
