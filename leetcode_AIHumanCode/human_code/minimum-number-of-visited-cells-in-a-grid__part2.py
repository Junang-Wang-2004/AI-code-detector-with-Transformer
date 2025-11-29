# Time:  O(m * n * log(m + n))
# Space: O(m * n)
from sortedcontainers import SortedList


# bfs, sorted list
class Solution2_TLE(object):
    def minimumVisitedCells(self, grid):
        """
        """
        m, n = len(grid), len(grid[0])
        sl1 = [SortedList(range(n)) for _ in range(m)]
        sl2 = [SortedList(range(m)) for _ in range(n)]
        d, i, j = 1, 0, 0
        q = [(i, j)]
        while q:
            new_q = []
            for i, j in q:
                if (i, j) == (m-1, n-1):
                    return d
                for k in list(sl1[i].irange(j+1, min(j+grid[i][j], n-1))):
                    new_q.append((i, k))
                    sl2[k].remove(i)
                    sl1[i].remove(k)
                for k in list(sl2[j].irange(i+1, min(i+grid[i][j], m-1))):
                    new_q.append((k, j))
                    sl1[k].remove(j)
                    sl2[j].remove(k)
            q = new_q
            d += 1
        return -1
