from sortedcontainers import SortedList

class C1(object):

    def shortestDistanceAfterQueries(self, a1, a2):
        """
        """
        v1 = SortedList(range(a1))
        v2 = []
        for v3, v4 in a2:
            for v5 in reversed(range(v1.bisect_right(v3), v1.bisect_left(v4))):
                v1.pop(v5)
            v2.append(len(v1) - 1)
        return v2
