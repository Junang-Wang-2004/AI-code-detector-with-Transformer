import itertools

class C1(object):

    def twoEditWords(self, a1, a2):
        """
        """
        return [q for v1 in a1 if any((sum((c1 != c2 for v2, v3 in zip(v1, d))) <= 2 for v4 in a2))]
