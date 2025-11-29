from sortedcontainers import SortedList

class C1(object):

    def minimumSumSubarray(self, a1, a2, a3):
        """
        """
        v1 = float('inf')
        v2 = [0] * (len(a1) + 1)
        for v3 in range(len(a1)):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = v1
        v5 = SortedList()
        for v3 in range(len(a1)):
            if v3 - a2 + 1 >= 0:
                v5.add(v2[v3 - a2 + 1])
            if v3 - a3 >= 0:
                v5.remove(v2[v3 - a3])
            v6 = v5.bisect_left(v2[v3 + 1]) - 1
            if v6 >= 0:
                v4 = min(v4, v2[v3 + 1] - v5[v6])
        return v4 if v4 != v1 else -1
