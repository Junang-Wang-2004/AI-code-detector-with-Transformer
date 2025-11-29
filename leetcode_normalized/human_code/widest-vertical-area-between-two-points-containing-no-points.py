import itertools

class C1(object):

    def maxWidthOfVerticalArea(self, a1):
        """
        """
        v1 = sorted({x for v2, v3 in a1})
        return max([b - a for v4, v5 in zip(v1, v1[1:])] + [0])
