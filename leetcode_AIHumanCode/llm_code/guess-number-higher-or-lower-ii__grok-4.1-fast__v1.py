class Solution:
    def getMoneyAmount(self, n):
        costs = [[0] * (n + 2) for _ in range(n + 2)]
        for length in range(2, n + 1):
            for begin in range(1, n - length + 2):
                finish = begin + length - 1
                lowest = float('inf')
                for pick in range(begin, finish + 1):
                    lcost = costs[begin][pick - 1]
                    rcost = costs[pick + 1][finish]
                    expense = pick + max(lcost, rcost)
                    lowest = min(lowest, expense)
                costs[begin][finish] = lowest
        return costs[1][n]
