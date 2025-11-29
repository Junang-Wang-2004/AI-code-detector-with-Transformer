class Solution:
    def findPath(self, grid, k):
        if not grid or not grid[0]:
            return []
        m, n = len(grid), len(grid[0])
        total = m * n
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col, expect, path, visited):
            cell_val = grid[row][col]
            if cell_val != 0 and cell_val != expect:
                return False
            path.append([row, col])
            visited[row][col] = True
            if len(path) == total:
                return True
            next_expect = expect + 1 if cell_val == expect else expect
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    if dfs(nr, nc, next_expect, path, visited):
                        return True
            path.pop()
            visited[row][col] = False
            return False

        for start_row in range(m):
            for start_col in range(n):
                visited = [[False] * n for _ in range(m)]
                current_path = []
                if dfs(start_row, start_col, 1, current_path, visited):
                    return current_path
        return []
