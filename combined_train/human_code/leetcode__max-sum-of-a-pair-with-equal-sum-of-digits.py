class C1(object):

    def maximumSum(self, a1):
        """
        """

        def sum_digits(a1):
            v1 = 0
            while a1:
                v1 += a1 % 10
                a1 //= 10
            return v1
        v1 = {}
        v2 = -1
        for v3 in a1:
            v4 = sum_digits(v3)
            if v4 not in v1:
                v1[v4] = v3
                continue
            v2 = max(v2, v1[v4] + v3)
            if v3 > v1[v4]:
                v1[v4] = v3
        return v2
