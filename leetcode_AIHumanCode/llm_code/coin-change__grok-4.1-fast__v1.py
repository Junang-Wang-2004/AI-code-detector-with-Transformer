class Solution:
    def coinChange(self, coins, amount):
        target = amount
        BIG = 10**9
        ways = [BIG] * (target + 1)
        ways[0] = 0
        for denom in coins:
            for total in range(denom, target + 1):
                ways[total] = min(ways[total], ways[total - denom] + 1)
        res = ways[target]
        return res if res < BIG else -1
