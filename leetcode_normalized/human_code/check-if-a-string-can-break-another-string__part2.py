import itertools

class C1(object):

    def checkIfCanBreak(self, a1, a2):
        """
        """
        return not {1, -1}.issubset(set((cmp(a, b) for v1, v2 in zip(sorted(a1), sorted(a2)))))
