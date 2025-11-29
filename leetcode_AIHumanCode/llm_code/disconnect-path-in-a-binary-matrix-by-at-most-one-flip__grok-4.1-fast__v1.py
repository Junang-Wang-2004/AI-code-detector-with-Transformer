class Solution:
    def isPossibleToCutPath(self, grid):
        m, n = len(grid), len(grid[0])
        reachable_from_start = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if i == 0 and j == 0:
                    reachable_from_start[i][j] = True
                elif i > 0 and reachable_from_start[i - 1][j] or j > 0 and reachable_from_start[i][j - 1]:
                    reachable_from_start[i][j] = True
        reachable_to_end = [[False] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    continue
                if i == m - 1 and j == n - 1:
                    reachable_to_end[i][j] = True
                elif i + 1 < m and reachable_to_end[i + 1][j] or j + 1 < n and reachable_to_end[i][j + 1]:
                    reachable_to_end[i][j] = True
        for k in range(1, m + n - 2):
            num_crossings = 0
            i_start = max(0, k - n + 1)
            i_end = min(k, m - 1)
            for i in range(i_start, i_end + 1):
                j = k - i
                if reachable_from_start[i][j] and reachable_to_end[i][j]:
                    num_crossings += 1
            if num_crossings <= 1:
                return True
        return False
