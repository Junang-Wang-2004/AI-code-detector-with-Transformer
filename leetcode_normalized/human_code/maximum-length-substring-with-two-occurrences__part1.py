class C1(object):

    def maximumLengthSubstring(self, a1):
        """
        """
        v1 = 2
        v2 = 0
        v3 = [0] * 26
        v4 = v5 = 0
        for v6, v7 in enumerate(a1):
            if v3[ord(v7) - ord('a')] == v1:
                v5 += 1
            v3[ord(v7) - ord('a')] += 1
            if v5:
                v3[ord(a1[v4]) - ord('a')] -= 1
                if v3[ord(a1[v4]) - ord('a')] == v1:
                    v5 -= 1
                v4 += 1
        return v6 - v4 + 1
