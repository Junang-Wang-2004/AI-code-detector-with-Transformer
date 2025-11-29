import itertools

class C1(object):

    def checkIfCanBreak(self, a1, a2):
        """
        """
        a1, a2 = (sorted(a1), sorted(a2))
        return all((a >= b for v3, v4 in zip(a1, a2))) or all((v3 <= v4 for v3, v4 in zip(a1, a2)))
