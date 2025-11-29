class C1(object):

    def longestCommonPrefix(self, a1):
        """
        """

        def lcp(a1, a2):
            if a1 < 0 or a2 >= len(a1):
                return 0
            v1, v2 = (a1[a1], a1[a2])
            for v3 in range(min(len(v1), len(v2))):
                if v1[v3] != v2[v3]:
                    return v3
            return v3 + 1
        v1 = [lcp(i, i + 1) for v2 in range(len(a1) - 1)]
        v3 = [0] * (len(v1) + 2)
        for v2 in reversed(range(len(v1))):
            v3[v2] = max(v3[v2 + 1], v1[v2])
        v4 = [0] * len(a1)
        v5 = 0
        for v2 in range(len(a1)):
            if v2 - 2 >= 0:
                v5 = max(v5, v1[v2 - 2])
            v4[v2] = max(v5, v3[v2 + 1], lcp(v2 - 1, v2 + 1))
        return v4
