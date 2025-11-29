class C1(object):

    def validUtf8(self, a1):
        """
        """
        v1 = 0
        for v2 in a1:
            if v1 == 0:
                if v2 >> 5 == 6:
                    v1 = 1
                elif v2 >> 4 == 14:
                    v1 = 2
                elif v2 >> 3 == 30:
                    v1 = 3
                elif v2 >> 7:
                    return False
            else:
                if v2 >> 6 != 2:
                    return False
                v1 -= 1
        return v1 == 0
