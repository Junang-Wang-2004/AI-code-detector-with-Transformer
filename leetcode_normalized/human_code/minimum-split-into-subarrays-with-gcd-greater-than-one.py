class C1(object):

    def minimumSplits(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1, v2 = (1, 0)
        for v3 in a1:
            v2 = gcd(v2, v3)
            if v2 == 1:
                v2 = v3
                v1 += 1
        return v1
