class C1(object):

    def longestNiceSubstring(self, a1):
        """
        """
        v1 = set(list(a1))
        v2 = -1
        v3 = ''
        for v4 in range(len(a1) + 1):
            if not (v4 == len(a1) or a1[v4] not in v1 or a1[v4].swapcase() not in v1):
                continue
            if v2 == -1 and v4 == len(a1):
                return a1
            v5 = self.longestNiceSubstring(a1[v2 + 1:v4])
            if len(v5) > len(v3):
                v3 = v5
            v2 = v4
        return v3
