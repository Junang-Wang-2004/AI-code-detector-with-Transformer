import collections
import bisect

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__idxs = collections.defaultdict(list)
        for v1, v2 in enumerate(a1):
            self.__idxs[v2].append(v1)

    def query(self, a1, a2, a3):
        """
        """
        return bisect.bisect_right(self.__idxs[a3], a2) - bisect.bisect_left(self.__idxs[a3], a1)
