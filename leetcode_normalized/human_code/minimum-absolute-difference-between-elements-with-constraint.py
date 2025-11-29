from sortedcontainers import SortedList

class C1(object):

    def minAbsoluteDifference(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = SortedList()
        for v3 in range(a2, len(a1)):
            v2.add(a1[v3 - a2])
            v4 = v2.bisect_left(a1[v3])
            if v4 - 1 >= 0:
                v1 = min(v1, a1[v3] - v2[v4 - 1])
            if v4 < len(v2):
                v1 = min(v1, v2[v4] - a1[v3])
        return v1
