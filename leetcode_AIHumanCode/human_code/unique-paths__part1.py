# Time:  O(m + n)
# Space: O(1)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        """
        def nCr(n, r):  # Time: O(n), Space: O(1)
            if n-r < r:
                r = n-r
            c = 1
            for k in range(1, r+1):
                c *= n-k+1
                c //= k
            return c

        return nCr((m-1)+(n-1), n-1)


