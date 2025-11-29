from sortedcontainers import SortedList

class C1(object):

    def minimumVisitedCells(self, a1):
        """
        """
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [SortedList(range(v2)) for v4 in range(v1)]
        v5 = [SortedList(range(v1)) for v4 in range(v2)]
        v6, v7, v8 = (1, 0, 0)
        v9 = [(v7, v8)]
        while v9:
            v10 = []
            for v7, v8 in v9:
                if (v7, v8) == (v1 - 1, v2 - 1):
                    return v6
                for v11 in list(v3[v7].irange(v8 + 1, min(v8 + a1[v7][v8], v2 - 1))):
                    v10.append((v7, v11))
                    v5[v11].remove(v7)
                    v3[v7].remove(v11)
                for v11 in list(v5[v8].irange(v7 + 1, min(v7 + a1[v7][v8], v1 - 1))):
                    v10.append((v11, v8))
                    v3[v11].remove(v8)
                    v5[v8].remove(v11)
            v9 = v10
            v6 += 1
        return -1
