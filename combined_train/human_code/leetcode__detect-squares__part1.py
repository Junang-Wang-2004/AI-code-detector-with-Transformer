import collections

class C1(object):

    def __init__(self):
        self.__x_to_ys = collections.defaultdict(set)
        self.__point_counts = collections.defaultdict(int)

    def add(self, a1):
        """
        """
        self.__x_to_ys[a1[0]].add(a1[1])
        self.__point_counts[tuple(a1)] += 1

    def count(self, a1):
        """
        """
        v1 = 0
        for v2 in self.__x_to_ys[a1[0]]:
            if v2 == a1[1]:
                continue
            v3 = v2 - a1[1]
            v1 += self.__point_counts[a1[0], v2] * self.__point_counts[a1[0] + v3, a1[1]] * self.__point_counts[a1[0] + v3, v2]
            v1 += self.__point_counts[a1[0], v2] * self.__point_counts[a1[0] - v3, a1[1]] * self.__point_counts[a1[0] - v3, v2]
        return v1
