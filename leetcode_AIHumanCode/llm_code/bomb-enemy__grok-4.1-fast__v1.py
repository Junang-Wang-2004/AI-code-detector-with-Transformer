class Solution:
    def maxKilledEnemies(self, grid):
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        enemies_l = [[0] * cols for _ in range(rows)]
        enemies_r = [[0] * cols for _ in range(rows)]
        enemies_u = [[0] * cols for _ in range(rows)]
        enemies_d = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            count = 0
            for j in range(cols):
                if grid[i][j] == 'W':
                    count = 0
                else:
                    enemies_l[i][j] = count
                    if grid[i][j] == 'E':
                        count += 1
            count = 0
            for j in range(cols - 1, -1, -1):
                if grid[i][j] == 'W':
                    count = 0
                else:
                    enemies_r[i][j] = count
                    if grid[i][j] == 'E':
                        count += 1
        
        for j in range(cols):
            count = 0
            for i in range(rows):
                if grid[i][j] == 'W':
                    count = 0
                else:
                    enemies_u[i][j] = count
                    if grid[i][j] == 'E':
                        count += 1
            count = 0
            for i in range(rows - 1, -1, -1):
                if grid[i][j] == 'W':
                    count = 0
                else:
                    enemies_d[i][j] = count
                    if grid[i][j] == 'E':
                        count += 1
        
        max_enemies = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0':
                    total = (enemies_l[i][j] + enemies_r[i][j] +
                             enemies_u[i][j] + enemies_d[i][j])
                    if total > max_enemies:
                        max_enemies = total
        return max_enemies
