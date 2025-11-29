class C1(object):

    def baseNeg2(self, a1):
        """
        """
        v1 = []
        while a1:
            v1.append(str(-a1 & 1))
            a1 = -(a1 >> 1)
        v1.reverse()
        return ''.join(v1) if v1 else '0'
