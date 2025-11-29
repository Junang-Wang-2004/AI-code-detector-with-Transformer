class C1(object):

    def sumOfTheDigitsOfHarshadNumber(self, a1):
        """
        """
        v1 = 0
        v2 = a1
        while v2:
            v2, v3 = divmod(v2, 10)
            v1 += v3
        return v1 if a1 % v1 == 0 else -1
