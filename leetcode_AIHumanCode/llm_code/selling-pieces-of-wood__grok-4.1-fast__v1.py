class Solution(object):
    def sellingWood(self, m, n, prices):
        memo = {}
        for height, width, cost in prices:
            key = (height, width)
            memo[key] = max(memo.get(key, 0), cost)
        
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                curr = (row, col)
                if curr not in memo:
                    memo[curr] = 0
                for p in range(1, row // 2 + 1):
                    memo[curr] = max(memo[curr], memo[(p, col)] + memo[(row - p, col)])
                for q in range(1, col // 2 + 1):
                    memo[curr] = max(memo[curr], memo[(row, q)] + memo[(row, col - q)])
        return memo[(m, n)]
