class Solution:
    def maximalNetworkRank(self, n, roads):
        degs = [0] * n
        linked = [[False] * n for _ in range(n)]
        for x, y in roads:
            degs[x] += 1
            degs[y] += 1
            linked[x][y] = True
            linked[y][x] = True
        best = 0
        for p in range(n):
            for q in range(p + 1, n):
                overlap = 1 if linked[p][q] else 0
                total = degs[p] + degs[q] - overlap
                best = max(best, total)
        return best
