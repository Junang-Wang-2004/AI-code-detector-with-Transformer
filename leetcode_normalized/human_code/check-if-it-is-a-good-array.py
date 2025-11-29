class C1(object):

    def isGoodArray(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = a1[0]
        for v2 in a1:
            v1 = gcd(v1, v2)
            if v1 == 1:
                break
        return v1 == 1
