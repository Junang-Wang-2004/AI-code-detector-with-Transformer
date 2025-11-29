class C1(object):

    def isSubsequence(self, a1, a2):
        """
        """
        if not a1:
            return True
        v1 = 0
        for v2 in a2:
            if v2 == a1[v1]:
                v1 += 1
            if v1 == len(a1):
                break
        return v1 == len(a1)
