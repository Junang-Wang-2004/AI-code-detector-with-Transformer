class C1(object):

    def findNumbers(self, a1):
        """
        """

        def digit_count(a1):
            v1 = 0
            while a1:
                a1 //= 10
                v1 += 1
            return v1
        return sum((digit_count(n) % 2 == 0 for v1 in a1))
