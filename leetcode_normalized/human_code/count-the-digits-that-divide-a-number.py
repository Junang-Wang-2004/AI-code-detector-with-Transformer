class C1(object):

    def countDigits(self, a1):
        """
        """
        v1 = 0
        v2 = a1
        while v2:
            v1 += int(a1 % (v2 % 10) == 0)
            v2 //= 10
        return v1
