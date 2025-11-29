class C1(object):

    def splitNum(self, a1):
        """
        """
        v1 = ''.join(sorted(str(a1)))
        return int(v1[::2]) + int(v1[1::2])
