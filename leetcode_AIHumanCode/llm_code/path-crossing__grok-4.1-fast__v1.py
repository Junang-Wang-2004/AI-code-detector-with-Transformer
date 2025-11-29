class Solution:
    def isPathCrossing(self, path):
        positions = [(0, 0)]
        rx, ry = 0, 0
        directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for step in path:
            dx, dy = directions[step]
            rx += dx
            ry += dy
            positions.append((rx, ry))
        return len(positions) != len(set(positions))
