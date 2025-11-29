class C1(object):

    def toHex(self, a1):
        """
        """
        if not a1:
            return '0'
        v1 = []
        while a1 and len(v1) != 8:
            v2 = a1 & 15
            if v2 < 10:
                v1.append(str(chr(ord('0') + v2)))
            else:
                v1.append(str(chr(ord('a') + v2 - 10)))
            a1 >>= 4
        v1.reverse()
        return ''.join(v1)
