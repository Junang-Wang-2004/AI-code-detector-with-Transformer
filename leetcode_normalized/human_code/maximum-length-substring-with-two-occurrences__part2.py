class C1(object):

    def maximumLengthSubstring(self, a1):
        """
        """
        v1 = 2
        v2 = 0
        v3 = [0] * 26
        v4 = 0
        for v5, v6 in enumerate(a1):
            v3[ord(v6) - ord('a')] += 1
            while v3[ord(v6) - ord('a')] > v1:
                v3[ord(a1[v4]) - ord('a')] -= 1
                v4 += 1
            v2 = max(v2, v5 - v4 + 1)
        return v2
