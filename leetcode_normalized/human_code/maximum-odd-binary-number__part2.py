class C1(object):

    def maximumOddBinaryNumber(self, a1):
        """
        """
        v1 = a1.count('1')
        return ''.join(['1'] * (v1 - 1) + ['0'] * (len(a1) - v1) + ['1'])
