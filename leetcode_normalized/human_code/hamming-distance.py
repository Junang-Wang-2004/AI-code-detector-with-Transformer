class C1(object):

    def hammingDistance(self, a1, a2):
        """
        """
        v1 = 0
        v2 = a1 ^ a2
        while v2:
            v1 += 1
            v2 &= v2 - 1
        return v1

    def hammingDistance2(self, a1, a2):
        """
        """
        return bin(a1 ^ a2).count('1')
