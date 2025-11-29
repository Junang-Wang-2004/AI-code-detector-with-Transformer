class C1(object):

    def isSubstringPresent(self, a1):
        """
        """
        v1 = [[False] * 26 for v2 in range(26)]
        for v3 in range(len(a1) - 1):
            v1[ord(a1[v3]) - ord('a')][ord(a1[v3 + 1]) - ord('a')] = True
        return any((v1[ord(a1[v3 + 1]) - ord('a')][ord(a1[v3]) - ord('a')] for v3 in range(len(a1) - 1)))
