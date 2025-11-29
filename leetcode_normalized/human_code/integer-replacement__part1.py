class C1(object):

    def integerReplacement(self, a1):
        """
        """
        v1 = 0
        while a1 != 1:
            v2 = a1 & 3
            if a1 == 3:
                a1 -= 1
            elif v2 == 3:
                a1 += 1
            elif v2 == 1:
                a1 -= 1
            else:
                a1 /= 2
            v1 += 1
        return v1
