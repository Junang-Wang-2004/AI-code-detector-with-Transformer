class C1(object):

    def sumOfDigits(self, a1):
        """
        """
        v1 = sum([int(c) for v2 in str(min(a1))])
        return 1 if v1 % 2 == 0 else 0
