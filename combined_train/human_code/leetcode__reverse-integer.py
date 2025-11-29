class C1(object):

    def reverse(self, a1):
        """
        """
        if a1 < 0:
            return -self.reverse(-a1)
        v1 = 0
        while a1:
            v1 = v1 * 10 + a1 % 10
            a1 //= 10
        return v1 if v1 <= 2147483647 else 0

    def reverse2(self, a1):
        """
        """
        if a1 < 0:
            a1 = int(str(a1)[::-1][-1] + str(a1)[::-1][:-1])
        else:
            a1 = int(str(a1)[::-1])
        a1 = 0 if abs(a1) > 2147483647 else a1
        return a1

    def reverse3(self, a1):
        """
        """
        v1 = cmp(a1, 0)
        v2 = int(repr(v1 * a1)[::-1])
        return v1 * v2 * (v2 < 2 ** 31)
