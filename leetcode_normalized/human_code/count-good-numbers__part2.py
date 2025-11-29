class C1(object):

    def countGoodNumbers(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        return pow(5, (a1 + 1) // 2 % (v1 - 1), v1) * pow(4, a1 // 2 % (v1 - 1), v1) % v1
