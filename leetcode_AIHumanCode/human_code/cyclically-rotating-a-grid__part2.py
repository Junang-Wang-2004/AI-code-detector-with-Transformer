# Time:  O(m * n)
# Space: O(1)
# inplace rotation
class Solution2(object):
    def rotateGrid(self, grid, k):
        """
        """
        def get_index(m, n, l):
            if l < m-1:
                return l, 0
            if l < (m-1)+(n-1):
                return m-1, l-(m-1)
            if l < (m-1)+(n-1)+(m-1):
                return (m-1)-(l-((m-1)+(n-1))), n-1
            return 0, (n-1)-(l-((m-1)+(n-1)+(m-1)))

        def reverse(grid, m, n, i, left, right):
            while left < right:
                lr, lc = get_index(m, n, left)
                rr, rc = get_index(m, n, right)
                grid[i+lr][i+lc], grid[i+rr][i+rc] = grid[i+rr][i+rc], grid[i+lr][i+lc]
                left += 1
                right -= 1

        m, n = len(grid), len(grid[0])
        for i in range(min(m, n)//2):
            total = 2*((m-1)+(n-1))
            nk = k%total
            reverse(grid, m, n, i, 0, total-1)
            reverse(grid, m, n, i, 0, nk-1)
            reverse(grid, m, n, i, nk, total-1)
            m, n = m-2, n-2
        return grid
