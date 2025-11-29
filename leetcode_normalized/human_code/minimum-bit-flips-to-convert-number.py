class C1(object):

    def minBitFlips(self, a1, a2):
        """
        """
        return bin(a1 ^ a2).count('1')
