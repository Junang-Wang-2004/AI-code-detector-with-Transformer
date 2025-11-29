import collections

class C1(object):

    def findBlackPixel(self, a1, a2):
        """
        """
        v1 = collections.Counter(list(map(tuple, a1)))
        v2 = [col.count('B') for v3 in zip(*a1)]
        return sum((a2 * list(zip(row, v2)).count(('B', a2)) for v4, v5 in v1.items() if v5 == a2 == v4.count('B')))
