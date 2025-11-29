# Time:  O((n^2 + m^2 + 4 * n * m) * n * m) = O(max(n, m)^3 * min(n, m))
# Space: O(n * m)
# brute force
class Solution7(object):
    def minimumSum(self, grid):
        """
        """
        def minimumArea(min_i, max_i, min_j, max_j):
            min_r, max_r, min_c, max_c = max_i+1, min_i-1, max_j+1, min_j-1
            for i in range(min_i, max_i+1):
                for j in range(min_j, max_j+1):
                    if grid[i][j] == 0:
                        continue
                    min_r, max_r, min_c, max_c = min(min_r, i), max(max_r, i), min(min_c, j), max(max_c, j)
            return (max_r-min_r+1)*(max_c-min_c+1) if min_r <= max_i else 0
    
        result = float("inf")
        for _ in range(4):
            for i in range(len(grid)-1):
                a = minimumArea(0, i, 0, len(grid[0])-1)
                for j in range(len(grid[0])-1):
                    b = minimumArea(i+1, len(grid)-1, 0, j)
                    c = minimumArea(i+1, len(grid)-1, j+1, len(grid[0])-1)
                    result = min(result, a+b+c)
            for i in range(len(grid)-2):
                a = minimumArea(0, i, 0, len(grid[0])-1)
                for j in range(i+1, len(grid)-1):
                    b = minimumArea(i+1, j, 0, len(grid[0])-1)
                    c = minimumArea(j+1, len(grid)-1, 0, len(grid[0])-1)
                    result = min(result, a+b+c)
            grid = list(zip(*grid[::-1]))
        return result
