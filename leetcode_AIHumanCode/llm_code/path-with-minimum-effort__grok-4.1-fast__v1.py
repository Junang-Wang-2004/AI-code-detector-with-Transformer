class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        def idx(r, c):
            return r * n + c
        candidates = []
        for r in range(m):
            for c in range(n):
                for dr, dc in ((1, 0), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if nr < m and nc < n:
                        cost = abs(heights[r][c] - heights[nr][nc])
                        candidates.append((cost, idx(r, c), idx(nr, nc)))
        candidates.sort()
        par = list(range(m * n))
        rnk = [0] * (m * n)
        def root(x):
            if par[x] != x:
                par[x] = root(par[x])
            return par[x]
        def merge(a, b):
            ra, rb = root(a), root(b)
            if ra == rb:
                return False
            if rnk[ra] < rnk[rb]:
                par[ra] = rb
            elif rnk[ra] > rnk[rb]:
                par[rb] = ra
            else:
                par[rb] = ra
                rnk[ra] += 1
            return True
        src = idx(0, 0)
        tgt = idx(m - 1, n - 1)
        for val, u, v in candidates:
            merge(u, v)
            if root(src) == root(tgt):
                return val
        return 0
