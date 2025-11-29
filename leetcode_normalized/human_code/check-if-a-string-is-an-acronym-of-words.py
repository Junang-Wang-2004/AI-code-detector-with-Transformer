import itertools

class C1(object):

    def isAcronym(self, a1, a2):
        """
        """
        return len(a1) == len(a2) and all((w[0] == c for v1, v2 in zip(a1, a2)))
