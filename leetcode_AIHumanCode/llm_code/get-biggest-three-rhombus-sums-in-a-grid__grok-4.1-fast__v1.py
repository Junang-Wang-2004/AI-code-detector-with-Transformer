class Solution:
    def getBiggestThree(self, grid):
        rows, cols = len(grid), len(grid[0])
        pref1 = [[0] * cols for _ in range(rows)]
        pref2 = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                pref1[i][j] = grid[i][j]
        for i in range(1, rows):
            for j in range(cols - 1):
                pref1[i][j] += pref1[i - 1][j + 1]
        for i in range(rows):
            for j in range(cols):
                pref2[i][j] = grid[i][j]
        for i in range(1, rows):
            for j in range(1, cols):
                pref2[i][j] += pref2[i - 1][j - 1]
        import heapq
        pq = []
        unq = set()
        lim = 3
        mxk = (min(rows, cols) + 1) // 2
        for sz in range(mxk):
            for x in range(sz, rows - sz):
                for y in range(sz, cols - sz):
                    if sz == 0:
                        val = grid[x][y]
                    else:
                        p1 = pref1[x][y - sz] - pref1[x - sz][y]
                        p2 = pref2[x][y + sz] - pref2[x - sz][y]
                        p3 = grid[x - sz][y]
                        up = p1 + p2 + p3
                        p4 = pref1[x + sz][y] - pref1[x][y + sz]
                        p5 = pref2[x + sz][y] - pref2[x][y - sz]
                        p6 = grid[x + sz][y]
                        dn = p4 + p5 - p6
                        val = up + dn
                    if val in unq:
                        continue
                    unq.add(val)
                    heapq.heappush(pq, val)
                    if len(pq) > lim:
                        heapq.heappop(pq)
                        unq.remove(pq[0])
        pq.sort(reverse=True)
        return pq
