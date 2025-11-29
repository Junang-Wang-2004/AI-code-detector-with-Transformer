# Time:  O(max(n, m)^2 * log(max(n, m)))
# Space: O(n * m)
# prefix sum, binary search
class Solution5(object):
    def minimumSum(self, grid):
        """
        """
        def binary_search(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left
        
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        def minimumArea(min_i, max_i, min_j, max_j):
            def count(x1, y1, x2, y2):
                cnt = prefix[x2][y2]
                if x1-1 >= 0:
                    cnt -= prefix[x1-1][y2]
                if y1-1 >= 0:
                    cnt -= prefix[x2][y1-1]
                if x1-1 >= 0 and y1-1 >= 0:
                    cnt += prefix[x1-1][y1-1]
                return cnt

            min_r = binary_search(min_i, max_i, lambda i: count(min_i, min_j, i, max_j))
            max_r = binary_search_right(min_i, max_i, lambda i: count(i, min_j, max_i, max_j))
            min_c = binary_search(min_j, max_j, lambda j: count(min_i, min_j, max_i, j))
            max_c = binary_search_right(min_j, max_j, lambda j: count(min_i, j, max_i, max_j))
            return (max_r-min_r+1)*(max_c-min_c+1) if min_r <= max_i else 0
    
        result = float("inf")
        for _ in range(4):
            prefix = [[0]*len(grid[0]) for _ in range(len(grid))]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    prefix[i][j] = grid[i][j]
                    if i-1 >= 0:
                        prefix[i][j] += prefix[i-1][j]
                    if j-1 >= 0:
                        prefix[i][j] += prefix[i][j-1]
                    if i-1 >= 0 and j-1 >= 0:
                        prefix[i][j] -= prefix[i-1][j-1]
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


