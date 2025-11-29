from functools import reduce
# Time:  O(h * p^2), p is the number of patterns
# Space: O(p^2)

# bitmask, backtracking, dp
class Solution(object):
    def buildWall(self, height, width, bricks):
        """
        """
        MOD = 10**9+7
        def backtracking(height, width, bricks, total, mask, lookup, patterns):
            if mask in lookup:
                return
            lookup.add(mask)
            if total >= width:
                if total == width:
                    patterns.append(mask^(1<<width))
                return
            for x in bricks:
                backtracking(height, width, bricks, total+x, mask|(1<<(total+x)), lookup, patterns)

        patterns, lookup = [], set()
        backtracking(height, width, bricks, 0, 0, lookup, patterns)
        adj = [[j for j, r2 in enumerate(patterns) if not (r1 & r2)] for r1 in patterns]
        dp = [[1]*len(patterns), [0]*len(patterns)]
        for i in range(height-1):
            dp[(i+1)%2] = [sum(dp[i%2][k] for k in adj[j]) % MOD for j in range(len(patterns))]
        return sum(dp[(height-1)%2]) % MOD


