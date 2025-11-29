class C1(object):

    def numberOfSubstrings(self, a1, a2):
        """
        """
        v1 = [0] * 26
        v2 = v3 = 0
        for v4 in range(len(a1)):
            v1[ord(a1[v4]) - ord('a')] += 1
            while v1[ord(a1[v4]) - ord('a')] == a2:
                v2 += len(a1) - 1 - v4 + 1
                v1[ord(a1[v3]) - ord('a')] -= 1
                v3 += 1
        return v2
