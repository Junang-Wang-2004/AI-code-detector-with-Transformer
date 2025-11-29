class C1(object):

    def sumOfNumberAndReverse(self, a1):
        """
        """

        def reverse(a1):
            v1 = 0
            while a1:
                v1 = v1 * 10 + a1 % 10
                a1 //= 10
            return v1
        return any((x + reverse(x) == a1 for v1 in range(a1 // 2, a1 + 1)))
