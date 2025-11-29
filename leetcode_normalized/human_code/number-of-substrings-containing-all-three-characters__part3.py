class C1(object):

    def numberOfSubstrings(self, a1):
        """
        """
        v1, v2, v3 = (0, 0, [0] * 3)
        for v4, v5 in enumerate(a1):
            while v2 < len(a1) and (not all(v3)):
                v3[ord(a1[v2]) - ord('a')] += 1
                v2 += 1
            if all(v3):
                v1 += len(a1) - 1 - (v2 - 1) + 1
            v3[ord(v5) - ord('a')] -= 1
        return v1
