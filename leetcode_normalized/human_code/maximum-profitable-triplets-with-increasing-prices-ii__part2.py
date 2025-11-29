from sortedcontainers import SortedList

class C1(object):

    def maxProfit(self, a1, a2):
        """
        """
        v1 = float('-inf')
        v2 = [v1] * len(a1)
        v3 = SortedList()
        for v4 in reversed(range(len(a1))):
            v5 = v3.bisect_left((-a1[v4],))
            if v5 - 1 >= 0:
                v2[v4] = v3[v5 - 1][1]
            if not (v5 - 1 < 0 or v3[v5 - 1][1] < a2[v4]):
                continue
            v3.add((-a1[v4], a2[v4]))
            v5 = v3.bisect_left((-a1[v4], a2[v4]))
            while v5 + 1 < len(v3) and v3[v5 + 1][1] <= v3[v5][1]:
                del v3[v5 + 1]
        v6 = v1
        v3 = SortedList()
        for v4 in range(len(a1)):
            v5 = v3.bisect_left((a1[v4],))
            if v5 - 1 >= 0:
                v6 = max(v6, v3[v5 - 1][1] + a2[v4] + v2[v4])
            if not (v5 - 1 < 0 or v3[v5 - 1][1] < a2[v4]):
                continue
            v3.add((a1[v4], a2[v4]))
            v5 = v3.bisect_left((a1[v4], a2[v4]))
            while v5 + 1 < len(v3) and v3[v5 + 1][1] <= v3[v5][1]:
                del v3[v5 + 1]
        return v6 if v6 != v1 else -1
