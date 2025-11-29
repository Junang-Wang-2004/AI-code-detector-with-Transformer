from functools import reduce

class C1(object):

    def arraysIntersection(self, a1, a2, a3):
        """
        """
        v1 = reduce(set.intersection, list(map(set, [a2, a3])))
        return [x for v2 in a1 if v2 in v1]
