import itertools

class C1(object):

    def heightChecker(self, a1):
        """
        """
        return sum((i != j for v1, v2 in zip(a1, sorted(a1))))
