class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1
        sub_max = [[0] * n for _ in range(n)]
        for start in range(n):
            mx = 0
            for finish in range(start, n):
                mx = max(mx, jobDifficulty[finish])
                sub_max[start][finish] = mx
        opt = [[float("inf")] * n for _ in range(d)]
        for pos in range(n):
            opt[0][pos] = sub_max[0][pos]
        for layer in range(1, d):
            for pos in range(layer, n):
                for prev in range(layer - 1, pos):
                    total = opt[layer - 1][prev] + sub_max[prev + 1][pos]
                    if total < opt[layer][pos]:
                        opt[layer][pos] = total
        return opt[d - 1][n - 1]
