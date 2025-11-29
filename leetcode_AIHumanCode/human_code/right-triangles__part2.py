# Time:  O(n * m)
# Space: O(n + m)
# combinatorics
class Solution2(object):
    def numberOfRightTriangles(self, grid):
        """
        """
        n, m = len(grid), len(grid[0])
        cnt1 = [sum(grid[i][j] for j in range(m)) for i in range(n)]
        cnt2 = [sum(grid[i][j] for i in range(n)) for j in range(m)]
        return sum((cnt1[i]-1)*(cnt2[j]-1) for i in range(n) for j in range(m) if grid[i][j])


