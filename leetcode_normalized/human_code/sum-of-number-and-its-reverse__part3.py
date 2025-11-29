class C1(object):

    def sumOfNumberAndReverse(self, a1):
        """
        """
        return any((x + int(str(x)[::-1]) == a1 for v1 in range(a1 // 2, a1 + 1)))
