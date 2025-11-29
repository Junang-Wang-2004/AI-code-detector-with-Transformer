from sortedcontainers import SortedList

class C1(object):

    def minAbsDiff(self, a1, a2):
        """
        """
        v1 = [[-1] * (len(a1[0]) - (a2 - 1)) for v2 in range(len(a1) - (a2 - 1))]
        v3 = SortedList((a1[0 + di][0 + dj] for v4 in range(a2) for v5 in range(a2)))
        for v6 in range(len(a1) - (a2 - 1)):
            v7 = SortedList(v3)
            for v8 in range(len(a1[0]) - (a2 - 1)):
                v9 = float('inf')
                v10 = float('-inf')
                for v11 in v7:
                    if v10 != float('-inf') and v10 != v11:
                        v9 = min(v9, v11 - v10)
                    v10 = v11
                v1[v6][v8] = v9 if v9 != float('inf') else 0
                if v8 + 1 == len(a1[0]) - (a2 - 1):
                    continue
                for v4 in range(a2):
                    v7.remove(a1[v6 + v4][v8])
                    v7.add(a1[v6 + v4][v8 + a2])
            if v6 + 1 == len(a1) - (a2 - 1):
                continue
            for v5 in range(a2):
                v3.remove(a1[v6][0 + v5])
                v3.add(a1[v6 + a2][0 + v5])
        return v1
