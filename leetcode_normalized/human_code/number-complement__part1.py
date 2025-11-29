class C1(object):

    def findComplement(self, a1):
        """
        """
        return 2 ** (len(bin(a1)) - 2) - 1 - a1
