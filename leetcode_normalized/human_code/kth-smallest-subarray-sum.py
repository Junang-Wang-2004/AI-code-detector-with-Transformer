class C1(object):

    def kthSmallestSubarraySum(self, a1, a2):
        """
        """

        def check(a1, a2, a3):
            v1 = v2 = v3 = 0
            for v4 in range(len(a1)):
                v2 += a1[v4]
                while v2 > a3:
                    v2 -= a1[v3]
                    v3 += 1
                v1 += v4 - v3 + 1
            return v1 >= a2
        v1, v2 = (min(a1), sum(a1))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(a1, a2, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
