# Time:  O(n * m)
# Space: O(min(n, m))

# combinatorics
class Solution(object):
    def numberOfRightTriangles(self, grid):
        """
        """
        def get(i, j):
            return grid[i][j] if n < m else grid[j][i]

        n, m = len(grid), len(grid[0])
        result = 0
        cnt1 = [sum(get(i, j) for j in range(max(n, m))) for i in range(min(n, m))]
        for j in range(max(n, m)):
            cnt2 = sum(get(i, j) for i in range(min(n, m)))
            result += sum((cnt1[i]-1)*(cnt2-1) for i in range(min(n, m)) if get(i, j))
        return result


