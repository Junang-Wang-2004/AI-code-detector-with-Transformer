class C1(object):

    def baseNeg2(self, a1):
        """
        """
        v1 = -2
        v2 = []
        while a1:
            a1, v4 = divmod(a1, v1)
            if v4 < 0:
                v4 -= v1
                a1 += 1
            v2.append(str(v4))
        v2.reverse()
        return ''.join(v2) if v2 else '0'
