class C1(object):

    def smallestNumber(self, a1, a2):
        """
        """

        def check(a1):
            v1 = 1
            while a1:
                v1 = v1 * (a1 % 10) % a2
                a1 //= 10
            return v1 == 0
        while not check(a1):
            a1 += 1
        return a1
