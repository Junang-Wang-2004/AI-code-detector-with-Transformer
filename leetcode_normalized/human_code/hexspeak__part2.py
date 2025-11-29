class C1(object):

    def toHexspeak(self, a1):
        """
        """
        v1 = hex(int(a1)).upper()[2:].replace('0', 'O').replace('1', 'I')
        return v1 if all((c in 'ABCDEFOI' for v2 in v1)) else 'ERROR'
