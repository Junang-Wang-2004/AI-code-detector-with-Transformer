class C1(object):

    def findLonelyPixel(self, a1):
        """
        """
        return sum((col.count('B') == 1 == a1[col.index('B')].count('B') for v1 in zip(*a1)))
