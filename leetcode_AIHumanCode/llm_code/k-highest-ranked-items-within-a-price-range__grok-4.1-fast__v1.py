from collections import deque

class Solution:
    def highestRankedKItems(self, grid, pricing, start, k):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])
        distances = [[float('inf')] * cols for _ in range(rows)]
        distances[start[0]][start[1]] = 0
        bfs_queue = deque([(start[0], start[1])])
        while bfs_queue:
            row, col = bfs_queue.popleft()
            for dr, dc in dirs:
                new_row = row + dr
                new_col = col + dc
                if (0 <= new_row < rows and
                    0 <= new_col < cols and
                    grid[new_row][new_col] != 0 and
                    distances[new_row][new_col] == float('inf')):
                    distances[new_row][new_col] = distances[row][col] + 1
                    bfs_queue.append((new_row, new_col))
        min_val, max_val = pricing
        valid_items = []
        for i in range(rows):
            for j in range(cols):
                if (min_val <= grid[i][j] <= max_val and
                    distances[i][j] < float('inf')):
                    valid_items.append((distances[i][j], grid[i][j], i, j))
        valid_items.sort()
        output = [[item[2], item[3]] for item in valid_items[:k]]
        return output
