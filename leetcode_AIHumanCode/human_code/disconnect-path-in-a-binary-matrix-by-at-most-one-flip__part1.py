# Time:  O(m * n)
# Space: O(m + n)

# dp
class Solution(object):
    def isPossibleToCutPath(self, grid):
        """
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) == (0, 0) or grid[i][j] == 0:
                    continue
                if (i-1 < 0 or grid[i-1][j] == 0) and (j-1 < 0 or grid[i][j-1] == 0):
                    grid[i][j] = 0
        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[0]))):
                if (i, j) == (len(grid)-1, len(grid[0])-1) or grid[i][j] == 0:
                    continue
                if (i+1 >= len(grid) or grid[i+1][j] == 0) and (j+1 >= len(grid[0]) or grid[i][j+1] == 0):
                    grid[i][j] = 0
        cnt = [0]*(len(grid)+len(grid[0])-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cnt[i+j] += grid[i][j]
        return any(cnt[i] <= 1 for i in range(1, len(grid)+len(grid[0])-2))


