class C1(object):

    def numberOfSpecialSubstrings(self, a1):
        """
        """
        v1 = v2 = 0
        v3 = [-1] * 26
        for v4 in range(len(a1)):
            if v3[ord(a1[v4]) - ord('a')] >= v2:
                v2 = v3[ord(a1[v4]) - ord('a')] + 1
            v3[ord(a1[v4]) - ord('a')] = v4
            v1 += v4 - v2 + 1
        return v1
