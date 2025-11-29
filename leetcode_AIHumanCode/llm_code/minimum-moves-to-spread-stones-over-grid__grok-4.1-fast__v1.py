class Solution(object):
    def minimumMoves(self, grid):
        m, n = len(grid), len(grid[0])
        supplies = []
        demands = []
        for i in range(m):
            for j in range(n):
                cnt = grid[i][j]
                if cnt == 0:
                    demands.append((i, j))
                elif cnt > 1:
                    for _ in range(cnt - 1):
                        supplies.append((i, j))
        import itertools
        ans = float('inf')
        k = len(demands)
        for matching in itertools.permutations(demands):
            cost = sum(abs(supplies[t][0] - matching[t][0]) + abs(supplies[t][1] - matching[t][1]) for t in range(k))
            ans = min(ans, cost)
        return int(ans)
