# Time:  O(m * n)
# Space: O(m + n)
# dfs
class Solution3(object):
    def isPossibleToCutPath(self, grid):
        """
        """
        def dfs(i, j):
            if not (i < len(grid) and j < len(grid[0]) and grid[i][j]):
                return False
            if (i, j) == (len(grid)-1, len(grid[0])-1):
                return True
            if (i, j) != (0, 0):
                grid[i][j] = 0
            return dfs(i+1, j) or dfs(i, j+1)

        return not dfs(0, 0) or not dfs(0, 0)
