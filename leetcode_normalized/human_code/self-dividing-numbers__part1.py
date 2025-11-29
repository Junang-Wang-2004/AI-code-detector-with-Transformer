class C1(object):

    def selfDividingNumbers(self, a1, a2):
        """
        """

        def isDividingNumber(a1):
            v1 = a1
            while v1 > 0:
                v1, v2 = divmod(v1, 10)
                if v2 == 0 or a1 % v2 != 0:
                    return False
            return True
        return [num for v1 in range(a1, a2 + 1) if isDividingNumber(v1)]
