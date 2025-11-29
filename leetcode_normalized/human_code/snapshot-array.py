import collections
import bisect

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__A = collections.defaultdict(lambda: [[0, 0]])
        self.__snap_id = 0

    def set(self, a1, a2):
        """
        """
        if self.__A[a1][-1][0] == self.__snap_id:
            self.__A[a1][-1][1] = a2
        else:
            self.__A[a1].append([self.__snap_id, a2])

    def snap(self):
        """
        """
        self.__snap_id += 1
        return self.__snap_id - 1

    def get(self, a1, a2):
        """
        """
        v1 = bisect.bisect_left(self.__A[a1], [a2 + 1, float('-inf')]) - 1
        return self.__A[a1][v1][1]
