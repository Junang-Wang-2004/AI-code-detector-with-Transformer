class Solution:
    def findCoins(self, numWays):
        coins = []
        length = len(numWays)
        ways = [1] + [0] * length
        for coin in range(1, length + 1):
            gap = numWays[coin - 1] - ways[coin]
            if gap == 1:
                coins.append(coin)
                for sum_val in range(coin, length + 1):
                    ways[sum_val] += ways[sum_val - coin]
            if numWays[coin - 1] != ways[coin]:
                return []
        return coins
