# Time:  O(n * m)
# Space: O(min(n, m))
# freq table
class Solution3(object):
    def numberOfRightTriangles(self, grid):
        """
        """
        def get(i, j):
            return grid[i][j] if n < m else grid[j][i]

        def count(direction):
            result = 0
            cnt = [0]*min(n, m)
            for j in direction(range(max(n, m))):
                c = sum(get(i, j) for i in range(len(cnt)))
                for i in range(len(cnt)):
                    if get(i, j) == 0:
                        continue
                    result += cnt[i]
                    cnt[i] += c-1
            return result
        
        n, m = len(grid), len(grid[0])
        return count(lambda x: x)+count(reversed)
