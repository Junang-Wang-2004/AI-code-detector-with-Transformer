class C1(object):

    def minBitwiseArray(self, a1):
        """
        """
        return [x - ((x + 1 & ~x) >> 1) if x & 1 else -1 for v1 in a1]
