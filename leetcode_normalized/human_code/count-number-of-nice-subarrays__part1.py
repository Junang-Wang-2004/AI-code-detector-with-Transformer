class C1(object):

    def numberOfSubarrays(self, a1, a2):
        """
        """

        def atMost(a1, a2):
            v1, v2, v3 = (0, 0, 0)
            for v4, v5 in enumerate(a1):
                v3 += v5 % 2
                while v3 > a2:
                    v3 -= a1[v2] % 2
                    v2 += 1
                v1 += v4 - v2 + 1
            return v1
        return atMost(a1, a2) - atMost(a1, a2 - 1)
