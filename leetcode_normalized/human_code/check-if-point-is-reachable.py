class C1(object):

    def isReachable(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = gcd(a1, a2)
        return v1 == v1 & ~(v1 - 1)
