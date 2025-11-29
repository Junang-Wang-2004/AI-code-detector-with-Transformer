class Solution(object):
    def minimumMoves(self, grid):
        n = len(grid)
        vis = set()
        que = [(0, 0, 0)]
        vis.add((0, 0, 0))
        dist = 0
        while que:
            nxt = []
            for row, col, ori in que:
                if row == n - 1 and col == n - 2 and ori == 0:
                    return dist
                if ori == 0:
                    if col + 2 < n and grid[row][col + 2] == 0:
                        st = (row, col + 1, 0)
                        if st not in vis:
                            vis.add(st)
                            nxt.append(st)
                    if row + 1 < n and grid[row + 1][col] == 0 and grid[row + 1][col + 1] == 0:
                        st1 = (row + 1, col, 0)
                        if st1 not in vis:
                            vis.add(st1)
                            nxt.append(st1)
                        st2 = (row, col, 1)
                        if st2 not in vis:
                            vis.add(st2)
                            nxt.append(st2)
                else:
                    if row + 2 < n and grid[row + 2][col] == 0:
                        st = (row + 1, col, 1)
                        if st not in vis:
                            vis.add(st)
                            nxt.append(st)
                    if col + 1 < n and grid[row][col + 1] == 0 and grid[row + 1][col + 1] == 0:
                        st1 = (row, col + 1, 1)
                        if st1 not in vis:
                            vis.add(st1)
                            nxt.append(st1)
                        st2 = (row, col, 0)
                        if st2 not in vis:
                            vis.add(st2)
                            nxt.append(st2)
            que = nxt
            dist += 1
        return -1
