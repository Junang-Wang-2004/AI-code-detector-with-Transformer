class C1(object):

    def numberOfSubstrings(self, a1):
        """
        """
        v1, v2, v3 = (0, 0, [0] * 3)
        for v4, v5 in enumerate(a1):
            v3[ord(a1[v4]) - ord('a')] += 1
            while all(v3):
                v3[ord(a1[v2]) - ord('a')] -= 1
                v2 += 1
            v1 += v2
        return v1
