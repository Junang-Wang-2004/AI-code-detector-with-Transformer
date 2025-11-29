class C1(object):

    def removeZeros(self, a1):
        """
        """
        v1 = ''.join((x for v2 in str(a1) if v2 != '0'))
        return int(v1) if v1 else 0
