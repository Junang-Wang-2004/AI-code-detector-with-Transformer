# Time:  O(m * n)
# Space: O(m * n)

import collections


# bfs
class Solution(object):
    def maximumMinutes(self, grid):
        """
        """
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        GRASS, FIRE, WALL, PERSON = list(range(4))
        INF = 10**9
        def bfs(grid):
            time = collections.defaultdict(int)
            d = 0
            q = [(r, c, FIRE) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == FIRE]
            q.append((0, 0, PERSON))
            while q:
                new_q = []
                for r, c, t in q:
                    for dr, dc in DIRECTIONS:
                        nr, nc = r+dr, c+dc
                        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and
                                grid[nr][nc] != WALL and
                                ((t == FIRE and grid[nr][nc] != FIRE) or
                                 (t == PERSON and (grid[nr][nc] == GRASS or (grid[nr][nc] == FIRE and (nr, nc) == (len(grid)-1, len(grid[0])-1) and d+1 == time[FIRE, nr, nc]))))):
                            continue
                        if grid[nr][nc] != FIRE:
                            grid[nr][nc] = t
                        if (nr, nc) in ((len(grid)-1, len(grid[0])-1), (len(grid)-1, len(grid[0])-2), (len(grid)-2, len(grid[0])-1)):
                            time[t, nr, nc] = d+1
                        new_q.append((nr, nc, t))
                q = new_q
                d += 1
            return time

        time = bfs(grid)
        if not time[PERSON, len(grid)-1, len(grid[0])-1]:
            return -1
        if not time[FIRE, len(grid)-1, len(grid[0])-1]:
            return INF
        diff = time[FIRE, len(grid)-1, len(grid[0])-1]-time[PERSON, len(grid)-1, len(grid[0])-1]
        return diff if diff+2 in (time[FIRE, len(grid)-1, len(grid[0])-2]-time[PERSON, len(grid)-1, len(grid[0])-2],
                                  time[FIRE, len(grid)-2, len(grid[0])-1]-time[PERSON, len(grid)-2, len(grid[0])-1]) else diff-1


