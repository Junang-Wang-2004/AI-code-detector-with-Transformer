class Solution:
    def specialGrid(self, n):
        sz = 1 << n
        grid = [[0] * sz for _ in range(sz)]
        
        def fill(r, c, length, num):
            if length == 1:
                grid[r][c] = num
                return num + 1
            half = length // 2
            num = fill(r, c + half, half, num)
            num = fill(r + half, c + half, half, num)
            num = fill(r + half, c, half, num)
            num = fill(r, c, half, num)
            return num
        
        fill(0, 0, sz, 0)
        return grid
