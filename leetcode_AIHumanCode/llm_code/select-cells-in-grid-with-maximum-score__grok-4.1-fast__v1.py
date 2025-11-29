class Solution:
    def maxScore(self, grid):
        n = len(grid)
        if n == 0:
            return 0
        flat = [num for row in grid for num in row]
        if not flat:
            return 0
        max_val = max(flat)
        rows_for_val = [[] for _ in range(max_val)]
        for i in range(n):
            for val in set(grid[i]):
                idx = val - 1
                if 0 <= idx < max_val:
                    rows_for_val[idx].append(i)
        N = 1 << n
        scores = [-float('inf')] * N
        scores[0] = 0
        for v in range(max_val):
            opts = rows_for_val[v]
            if not opts:
                continue
            for msk in range(N - 1, -1, -1):
                val_here = scores[msk]
                if val_here == -float('inf'):
                    continue
                for r in opts:
                    if (msk & (1 << r)) == 0:
                        nmsk = msk | (1 << r)
                        scores[nmsk] = max(scores[nmsk], val_here + v + 1)
        return max(scores)
