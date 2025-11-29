class C1(object):

    def maxSubstringLength(self, a1):
        """
        """

        def check(a1, a2):
            return all((a1 <= left[ord(a1[i]) - ord('a')] and right[ord(a1[i]) - ord('a')] <= a2 for v1 in range(a1, a2 + 1)))
        v1, v2 = ([-1] * 26, [-1] * 26)
        for v3, v4 in enumerate(a1):
            v4 = ord(v4) - ord('a')
            if v1[v4] == -1:
                v1[v4] = v3
            v2[v4] = v3
        v5 = -1
        for v6 in v1:
            if v6 == -1:
                continue
            for v7 in v2:
                if v7 == -1:
                    continue
                if v6 <= v7 and v5 < v7 - v6 + 1 != len(a1) and check(v6, v7):
                    v5 = v7 - v6 + 1
        return v5
