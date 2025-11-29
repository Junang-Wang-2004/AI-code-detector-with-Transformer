class C1(object):

    def smallestNumber(self, a1):
        """
        """
        return (1 << a1.bit_length()) - 1
