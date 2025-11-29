from collections import deque

class Solution:
    def hasPath(self, maze, start, destination):
        rows = len(maze)
        if rows == 0:
            return False
        cols = len(maze[0])
        src = tuple(start)
        tgt = tuple(destination)
        vis = set([src])
        q = deque([src])
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            cr, cc = q.popleft()
            if (cr, cc) == tgt:
                return True
            for dr, dc in deltas:
                nr, nc = cr, cc
                while (0 <= nr + dr < rows and
                       0 <= nc + dc < cols and
                       maze[nr + dr][nc + dc] == 0):
                    nr += dr
                    nc += dc
                if (nr, nc) not in vis:
                    vis.add((nr, nc))
                    q.append((nr, nc))
        return False
