class C1(object):

    def sumOfMultiples(self, a1):
        """
        """

        def f(a1):
            return a1 * ((1 + a1 // a1) * (a1 // a1) // 2)
        return f(3) + f(5) + f(7) - (f(3 * 5) + f(5 * 7) + f(7 * 3)) + f(3 * 5 * 7)
