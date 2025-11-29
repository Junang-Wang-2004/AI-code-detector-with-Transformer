from sortedcontainers import SortedList

class C1(object):

    def maximumSegmentSum(self, a1, a2):
        """
        """
        v1 = SortedList([-1, len(a1)])
        v2 = [0] * (len(a1) + 1)
        for v3 in range(len(a1)):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = SortedList([v2[-1]])
        v5 = []
        for v6 in a2:
            v1.add(v6)
            v3 = v1.bisect_left(v6)
            v7, v8 = (v1[v3 - 1], v1[v3 + 1])
            v4.remove(v2[v8] - v2[v7 + 1])
            v4.add(v2[v6] - v2[v7 + 1])
            v4.add(v2[v8] - v2[v6 + 1])
            v5.append(v4[-1])
        return v5
