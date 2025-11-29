# Time:  O(10 * 2^4 * logn)
# Space: O(2^3)

# dp
class Solution(object):
    def countNoZeroPairs(self, n):
        """
        """
        dp = [[[0]*2 for _ in range(2)] for _ in range(2)]  # dp[carry][a is finished][b is finished]
        dp[0][0][0] = 1
        start = 1
        while n:
            n, d = divmod(n, 10)
            new_dp = [[[0]*2 for _ in range(2)] for _ in range(2)]
            for c in range(2):
                for i in range(2):
                    for j in range(2):
                        if not dp[c][i][j]:
                            continue
                        for x in range(start, (9 if not i else 0)+1):
                            for nc in range(2):
                                y = (d+nc*10)-(c+x)
                                if not (start <= y <= (9 if not j else 0)):
                                    continue
                                new_dp[nc][i or not x][j or not y] += dp[c][i][j]
            start = 0
            dp = new_dp
        return sum(dp[0][i][j] for i in range(2) for j in range(2))


