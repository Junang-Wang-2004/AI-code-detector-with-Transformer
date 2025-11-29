import collections

class C1(object):

    def twoOutOfThree(self, a1, a2, a3):
        """
        """
        v1 = 2
        v2 = collections.Counter()
        for v3 in (a1, a2, a3):
            v2.update(set(v3))
        return [x for v4, v5 in v2.items() if v5 >= v1]
