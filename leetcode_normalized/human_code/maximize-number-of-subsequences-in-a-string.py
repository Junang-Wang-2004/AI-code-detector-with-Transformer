class C1(object):

    def maximumSubsequenceCount(self, a1, a2):
        """
        """
        v1 = v2 = v3 = 0
        for v4 in a1:
            if v4 == a2[1]:
                v1 += v2
                v3 += 1
            if v4 == a2[0]:
                v2 += 1
        return v1 + max(v2, v3)
