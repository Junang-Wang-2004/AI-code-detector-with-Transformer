class C1(object):

    def minElement(self, a1):
        """
        """

        def f(a1):
            v1 = 0
            while a1:
                v1 += a1 % 10
                a1 //= 10
            return v1
        return min((f(x) for v1 in a1))
