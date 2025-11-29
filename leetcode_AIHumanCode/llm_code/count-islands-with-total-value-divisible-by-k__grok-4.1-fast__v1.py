class Solution(object):
    def countIslands(self, grid, k):
        m = len(grid)
        n = len(grid[0]) if m else 0
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def flood(start_x, start_y):
            accum = grid[start_x][start_y] % k
            pile = [(start_x, start_y)]
            grid[start_x][start_y] = 0
            while pile:
                cur_x, cur_y = pile.pop()
                for dx, dy in delta:
                    next_x = cur_x + dx
                    next_y = cur_y + dy
                    if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y]:
                        accum = (accum + grid[next_x][next_y]) % k
                        grid[next_x][next_y] = 0
                        pile.append((next_x, next_y))
            return accum == 0

        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    if flood(row, col):
                        ans += 1
        return ans
