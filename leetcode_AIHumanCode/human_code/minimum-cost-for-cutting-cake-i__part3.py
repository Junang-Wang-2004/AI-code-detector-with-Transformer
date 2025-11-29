# Time:  O((m + n) * m^2 * n^2)
# Space: O(m^2 * n^2)
# memoization
class Solution3(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        """
        def memoization(x1, y1, x2, y2):
            if (x1, y1) == (x2, y2):
                return 0
            if lookup[x1][y1][x2][y2] == -1:
                mn = float("inf")
                for x in range(x1, x2):
                    mn = min(ret, memoization(x1, y1, x, y2)+memoization(x+1, y1, x2, y2)+horizontalCut[x])
                for y in range(y1, y2):
                    mn = min(ret, memoization(x1, y1, x2, y)+memoization(x1, y+1, x2, y2)+verticalCut[y])
                lookup[x1][y1][x2][y2] = mn
            return lookup[x1][y1][x2][y2]

        lookup = [[[[-1]*n for _ in range(m)]for _ in range(n)] for _ in range(m)]
        return memoization(0, 0, m-1, n-1)

