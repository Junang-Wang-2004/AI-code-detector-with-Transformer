import collections

class C1(object):

    def minSteps(self, a1, a2):
        """
        """
        v1, v2 = (collections.Counter(a1), collections.Counter(a2))
        return sum((v1 - v2).values()) + sum((v2 - v1).values())
