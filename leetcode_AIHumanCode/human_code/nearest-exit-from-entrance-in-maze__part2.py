# Time:  O(m * n)
# Space: O(m + n)
# bfs solution
class Solution2(object):
    def nearestExit(self, maze, entrance):
        """
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = ' '
        entrance = tuple(entrance)
        maze[entrance[0]][entrance[1]] = visited
        q = [(entrance, 0)]
        while q:
            new_q = []
            for (r, c), step in q:
                if (r, c) != entrance and \
                   (r in (0, len(maze)-1) or c in (0, len(maze[0])-1)):
                    return step
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < len(maze) and
                            0 <= nc < len(maze[0]) and
                            maze[nr][nc] == '.'):
                        continue
                    maze[nr][nc] = visited
                    q.append(((nr, nc), step+1))
            q = new_q
        return -1
