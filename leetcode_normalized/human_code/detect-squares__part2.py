import collections

class C1(object):

    def __init__(self):
        self.__points = []
        self.__point_counts = collections.defaultdict(int)

    def add(self, a1):
        """
        """
        self.__points.append(a1)
        self.__point_counts[tuple(a1)] += 1

    def count(self, a1):
        """
        """
        v1 = 0
        for v2, v3 in self.__points:
            if not (a1[0] != v2 and a1[1] != v3 and (abs(a1[0] - v2) == abs(a1[1] - v3))):
                continue
            v1 += self.__point_counts[a1[0], v3] * self.__point_counts[v2, a1[1]]
        return v1
