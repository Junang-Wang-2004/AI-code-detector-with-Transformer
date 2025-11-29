from sortedcontainers import SortedList

class C1(object):

    def minAbsoluteDifference(self, a1, a2):
        v1 = SortedList()
        v2 = float('inf')
        v3 = 0
        for v4 in range(len(a1)):
            while v3 <= v4 - a2:
                v1.add(a1[v3])
                v3 += 1
            if v4 >= a2:
                v5 = v1.bisect_left(a1[v4])
                v6 = a1[v4] - v1[v5 - 1] if v5 > 0 else float('inf')
                v7 = v1[v5] - a1[v4] if v5 < len(v1) else float('inf')
                v2 = min(v2, v6, v7)
        return v2
