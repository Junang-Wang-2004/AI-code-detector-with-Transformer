class C1(object):

    def bitwiseComplement(self, a1):
        """
        """
        v1 = 1
        while a1 > v1:
            v1 = v1 * 2 + 1
        return v1 - a1
