class Solution:
    def isThereAPath(self, grid):
        rows, cols = len(grid), len(grid[0])
        path_len = rows + cols - 1
        if path_len % 2 != 0:
            return False
        target = path_len // 2

        # Minimum path sum using 1D DP
        min_path = [float('inf')] * cols
        min_path[0] = grid[0][0]
        for j in range(1, cols):
            min_path[j] = min_path[j - 1] + grid[0][j]
        for i in range(1, rows):
            min_path[0] += grid[i][0]
            for j in range(1, cols):
                min_path[j] = grid[i][j] + min(min_path[j], min_path[j - 1])
        min_total = min_path[-1]

        # Maximum path sum using 1D DP
        max_path = [float('-inf')] * cols
        max_path[0] = grid[0][0]
        for j in range(1, cols):
            max_path[j] = max_path[j - 1] + grid[0][j]
        for i in range(1, rows):
            max_path[0] += grid[i][0]
            for j in range(1, cols):
                max_path[j] = grid[i][j] + max(max_path[j], max_path[j - 1])
        max_total = max_path[-1]

        return min_total <= target <= max_total
