class C1(object):

    def mirrorReflection(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = a1 * a2 // gcd(a1, a2)
        if v1 // a1 % 2 == 1:
            if v1 // a2 % 2 == 1:
                return 1
            return 2
        return 0
