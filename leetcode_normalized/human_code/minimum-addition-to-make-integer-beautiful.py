class C1(object):

    def makeIntegerBeautiful(self, a1, a2):
        """
        """
        v1, v2 = (0, a1)
        while v2:
            v1 += v2 % 10
            v2 //= 10
        v2, v3 = (a1, 0)
        while v1 > a2:
            while True:
                v1 -= v2 % 10
                v2 //= 10
                v3 += 1
                if v2 % 10 != 9:
                    break
            v1 += 1
            v2 += 1
        return v2 * 10 ** v3 - a1
