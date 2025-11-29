class C1(object):

    def maximum69Number(self, a1):
        """
        """
        v1, v2, v3 = (a1, 3, 0)
        while v1:
            if v1 % 10 == 6:
                v3 = v2
            v2 *= 10
            v1 //= 10
        return a1 + v3
