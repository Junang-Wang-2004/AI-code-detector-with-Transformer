class C1(object):

    def maxPalindromesAfterOperations(self, a1):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            for v3 in v2:
                v1[ord(v3) - ord('a')] += 1
        v4 = sum((x // 2 for v5 in v1))
        for v6, v7 in enumerate(sorted(map(len, a1))):
            v4 -= v7 // 2
            if v4 < 0:
                return v6
        return len(a1)
