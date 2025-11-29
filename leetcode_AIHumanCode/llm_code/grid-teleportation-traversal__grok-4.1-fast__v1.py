from collections import deque, defaultdict
import math

class Solution:
    def minMoves(self, matrix):
        rows = len(matrix)
        if rows == 0:
            return -1
        cols = len(matrix[0])
        portals = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j].isupper():
                    portals[matrix[i][j]].append((i, j))
        costs = [[math.inf] * cols for _ in range(rows)]
        costs[0][0] = 0
        queue = deque([(0, 0)])
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.popleft()
            distance = costs[x][y]
            if x == rows - 1 and y == cols - 1:
                return distance
            cell = matrix[x][y]
            if cell.isupper():
                for nx, ny in portals[cell]:
                    if costs[nx][ny] > distance:
                        costs[nx][ny] = distance
                        queue.appendleft((nx, ny))
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != '#':
                    new_dist = distance + 1
                    if new_dist < costs[nx][ny]:
                        costs[nx][ny] = new_dist
                        queue.append((nx, ny))
        return -1
