# Time:  O(max(x^y)) = O((n/2)^(n/2))) = O(5^5), n = len(grid)*len(grid[0]), y = len(zero), x = n-y
# Space: O(y) = O(n) = O(9) = O(1)
# backtracking
class Solution3(object):
    def minimumMoves(self, grid):
        """
        """
        def dist(a, b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])

        def backtracking(curr):
            if curr == len(zero):
                return 0
            result = float("inf")
            i, j = zero[curr]
            for ni in range(len(grid)):
                for nj in range(len(grid[0])):
                    if not (grid[ni][nj] >= 2):
                        continue
                    grid[ni][nj] -= 1
                    result = min(result, dist((i, j), (ni, nj))+backtracking(curr+1))
                    grid[ni][nj] += 1
            return result

        zero = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0]
        return backtracking(0)
