class C1(object):

    def superPow(self, a1, a2):
        """
        """

        def myPow(a1, a2, a3):
            v1 = 1
            v2 = a1 % a3
            while a2:
                if a2 & 1:
                    v1 = v1 * v2 % a3
                a2 >>= 1
                v2 = v2 * v2 % a3
            return v1 % a3
        v1 = 1
        for v2 in a2:
            v1 = myPow(v1, 10, 1337) * myPow(a1, v2, 1337) % 1337
        return v1
