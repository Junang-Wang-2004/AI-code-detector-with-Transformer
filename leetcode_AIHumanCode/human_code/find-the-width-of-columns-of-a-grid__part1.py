# Time:  O(m * n)
# Space: O(1)

# array
class Solution(object):
    def findColumnWidth(self, grid):
        """
        """
        def length(x):
            l = 1
            if x < 0:
                x = -x
                l += 1
            while x >= 10:
                x //= 10
                l += 1
            return l

        return [max(length(grid[i][j]) for i in range(len(grid))) for j in range(len(grid[0]))]


