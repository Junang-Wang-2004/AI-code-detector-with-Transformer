# Time:  O(m * n)
# Space: O(m + n)
# iterative dfs
class Solution2(object):
    def isPossibleToCutPath(self, grid):
        """
        """
        def iter_dfs():
            stk = [(0, 0)]
            while stk:
                i, j = stk.pop()
                if not (i < len(grid) and j < len(grid[0]) and grid[i][j]):
                    continue
                if (i, j) == (len(grid)-1, len(grid[0])-1):
                    return True
                if (i, j) != (0, 0):
                    grid[i][j] = 0
                stk.append((i, j+1))
                stk.append((i+1, j))  
            return False

        return not iter_dfs() or not iter_dfs()


