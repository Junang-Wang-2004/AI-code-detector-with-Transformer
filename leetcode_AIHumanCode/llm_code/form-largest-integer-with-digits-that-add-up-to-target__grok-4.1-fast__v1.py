class Solution(object):
    def largestNumber(self, cost, target):
        dp = [-1] * (target + 1)
        dp[0] = 0
        for pos in range(target):
            if dp[pos] == -1:
                continue
            for k in range(9):
                nxt = pos + cost[k]
                if nxt > target:
                    continue
                dp[nxt] = max(dp[nxt], dp[pos] + 1)
        if dp[target] == -1:
            return "0"
        ans = []
        remain = target
        for d in range(9, 0, -1):
            val = cost[d - 1]
            while remain >= val and dp[remain] == dp[remain - val] + 1:
                ans.append(str(d))
                remain -= val
        return "".join(ans)
