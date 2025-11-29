class C1(object):

    def stringCount(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        return (pow(26, a1, v1) - (25 + 25 + 25 + a1) * pow(25, a1 - 1, v1) + (24 + 24 + 24 + a1 + a1 + 0) * pow(24, a1 - 1, v1) - (23 + a1 + 0 + 0) * pow(23, a1 - 1, v1)) % v1
