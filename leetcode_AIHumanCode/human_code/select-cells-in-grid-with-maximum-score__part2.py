# Time:  O(r + (n * m) * 2^n), r = max(x for row in grid for x in row)
# Space: O(r + n * m + 2^n)
# dp, bitmasks
class Solution2(object):
    def maxScore(self, grid):
        """
        """
        mx = max(x for row in grid for x in row)
        lookup = [set() for _ in range(mx)]
        for i, row in enumerate(grid):
            for x in row:
                lookup[x-1].add(i)
        dp = [float("-inf")]*(1<<len(grid))
        dp[0] = 0
        for x in range(len(lookup)):
            if not lookup[x]:
                continue
            for mask in reversed(range(len(dp))):
                for i in lookup[x]:
                    if mask&(1<<i):
                        continue
                    dp[mask|(1<<i)] = max(dp[mask|(1<<i)], dp[mask]+(x+1))
        return max(dp)
