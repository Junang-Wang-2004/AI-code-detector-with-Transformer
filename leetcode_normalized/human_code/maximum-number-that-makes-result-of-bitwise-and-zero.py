class C1(object):

    def maxNumber(self, a1):
        """
        """
        return (1 << a1.bit_length() - 1) - 1
