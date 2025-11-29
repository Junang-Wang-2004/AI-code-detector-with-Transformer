# Time:  O(n * m)
# Space: O(n * m)
# memoization
class Solution2(object):
    def lenOfVDiagonal(self, grid):
        """
        """
        def memoization(i, j, x, d, k):
            if not (0 <= i < n and 0 <= j < m):
                return 0
            if grid[i][j] != x:
                return 0
            if lookup[k][x][d][i][j] == 0:
                ni, nj = i+directions[d][0], j+directions[d][1]
                nx = 0 if x == 2 else 2
                result = memoization(ni, nj, nx, d, k)+1
                if k != 1:
                    nd = (d+1)%4
                    result = max(result, memoization(ni, nj, nx, nd, k+1)+1)
                lookup[k][x][d][i][j] = result
            return lookup[k][x][d][i][j]

        n, m = len(grid), len(grid[0])
        directions = ((1, 1), (1, -1), (-1, -1), (-1, 1))
        lookup = [[[[[0]*m for _ in range(n)] for _ in range(4)] for _ in range(3)] for _ in range(2)]  # be careful with the order, going from smaller dimensions to larger dimensions
        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in range(4):
                        result = max(result, memoization(i, j, 1, d, 0))
        return result
