from sortedcontainers import SortedList

class C1(object):

    def maximumTripletValue(self, a1):
        """
        """
        v1 = SortedList()
        v2 = [0] * len(a1)
        for v3 in reversed(range(1, len(a1) - 1)):
            v2[v3] = max(v2[v3 + 1], a1[v3 + 1])
        v4 = 0
        for v3 in range(1, len(a1) - 1):
            v1.add(a1[v3 - 1])
            v5 = v1.bisect_left(a1[v3])
            if v5 - 1 >= 0 and v2[v3] > a1[v3]:
                v4 = max(v4, v1[v5 - 1] - a1[v3] + v2[v3])
        return v4
