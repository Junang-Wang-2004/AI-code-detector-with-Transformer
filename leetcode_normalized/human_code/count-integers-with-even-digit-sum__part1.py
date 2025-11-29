class C1(object):

    def countEven(self, a1):
        """
        """

        def parity(a1):
            v1 = 0
            while a1:
                v1 += a1 % 10
                a1 //= 10
            return v1 % 2
        return (a1 - parity(a1)) // 2
