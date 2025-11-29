class C1(object):

    def maxSum(self, a1):
        """
        """

        def max_digit(a1):
            v1 = 0
            while a1:
                a1, v3 = divmod(a1, 10)
                v1 = max(v1, v3)
            return v1
        v1 = -1
        v2 = {}
        for v3 in a1:
            v4 = max_digit(v3)
            if v4 not in v2:
                v2[v4] = v3
                continue
            v1 = max(v1, v2[v4] + v3)
            v2[v4] = max(v2[v4], v3)
        return v1
