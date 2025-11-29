# Time:  O(m * n)
# Space: O(logr)
# array
class Solution2(object):
    def findColumnWidth(self, grid):
        """
        """
        return [max(len(str(grid[i][j])) for i in range(len(grid))) for j in range(len(grid[0]))]


