class C1(object):

    def maxNiceDivisors(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        if a1 <= 3:
            return a1
        if a1 % 3 == 0:
            return pow(3, a1 // 3, v1)
        if a1 % 3 == 1:
            return 2 * 2 * pow(3, (a1 - 4) // 3, v1) % v1
        return 2 * pow(3, (a1 - 2) // 3, v1) % v1
