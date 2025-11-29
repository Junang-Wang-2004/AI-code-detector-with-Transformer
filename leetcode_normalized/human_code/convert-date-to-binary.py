class C1(object):

    def convertDateToBinary(self, a1):
        """
        """
        return '-'.join([bin(int(x))[2:] for v1 in a1.split('-')])
