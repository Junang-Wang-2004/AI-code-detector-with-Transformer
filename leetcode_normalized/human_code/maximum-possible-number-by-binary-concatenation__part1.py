class C1(object):

    def maxGoodNumber(self, a1):
        """
        """
        return int(''.join(sorted([bin(x)[2:] for v1 in a1], cmp=lambda x, y: (v1 + y > y + v1) - (v1 + y < y + v1), reverse=True)), 2)
