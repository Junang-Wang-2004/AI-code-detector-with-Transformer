import itertools

class C1(object):

    def areSentencesSimilar(self, a1, a2, a3):
        """
        """
        if len(a1) != len(a2):
            return False
        v1 = set(map(tuple, a3))
        return all((w1 == w2 or (w1, w2) in v1 or (w2, w1) in v1 for v2, v3 in zip(a1, a2)))
