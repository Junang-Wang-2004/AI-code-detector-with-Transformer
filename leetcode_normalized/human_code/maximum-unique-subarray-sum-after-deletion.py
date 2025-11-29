class C1(object):

    def maxSum(self, a1):
        """
        """
        v1 = max(a1)
        return v1 if v1 < 0 else sum((x for v2 in set(a1) if v2 >= 0))
