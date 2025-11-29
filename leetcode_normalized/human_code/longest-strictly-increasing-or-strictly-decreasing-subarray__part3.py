class C1(object):

    def longestMonotonicSubarray(self, a1):
        """
        """

        def f(a1):
            v1 = v2 = 0
            for v3 in range(len(a1)):
                v2 += 1
                if v3 + 1 == len(a1) or not a1(a1[v3], a1[v3 + 1]):
                    v1 = max(v1, v2)
                    v2 = 0
            return v1
        return max(f(lambda x, y: x < y), f(lambda x, y: x > y))
