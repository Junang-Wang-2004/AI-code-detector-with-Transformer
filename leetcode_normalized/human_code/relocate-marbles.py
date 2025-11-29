import itertools

class C1(object):

    def relocateMarbles(self, a1, a2, a3):
        """
        """
        v1 = set(a1)
        for v2, v3 in zip(a2, a3):
            v1.remove(v2)
            v1.add(v3)
        return sorted(v1)
