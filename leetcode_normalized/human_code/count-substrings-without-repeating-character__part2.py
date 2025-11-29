class C1(object):

    def numberOfSpecialSubstrings(self, a1):
        """
        """
        v1 = v2 = 0
        v3 = [False] * 26
        for v4 in range(len(a1)):
            while v3[ord(a1[v4]) - ord('a')]:
                v3[ord(a1[v2]) - ord('a')] = False
                v2 += 1
            v3[ord(a1[v4]) - ord('a')] = True
            v1 += v4 - v2 + 1
        return v1
