class C1(object):

    def canMakeSubsequence(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in a1:
            if (ord(a2[v1]) - ord(v2)) % 26 > 1:
                continue
            v1 += 1
            if v1 == len(a2):
                return True
        return False
