class C1(object):

    def replaceNonCoprimes(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = []
        for v2 in a1:
            while True:
                v3 = gcd(v1[-1] if v1 else 1, v2)
                if v3 == 1:
                    break
                v2 *= v1.pop() // v3
            v1.append(v2)
        return v1
