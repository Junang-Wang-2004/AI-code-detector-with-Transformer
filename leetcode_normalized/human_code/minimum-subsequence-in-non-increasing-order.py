class C1(object):

    def minSubsequence(self, a1):
        """
        """
        v1, v2, v3 = ([], sum(a1), 0)
        a1.sort(reverse=True)
        for v4, v5 in enumerate(a1):
            v3 += v5
            if v3 > v2 - v3:
                break
        return a1[:v4 + 1]
