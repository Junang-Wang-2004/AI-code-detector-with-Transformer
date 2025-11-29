class Solution:
    def maxCoins(self, nums):
        balloons = [1] + nums + [1]
        size = len(balloons)
        memo = [[-1] * size for _ in range(size)]

        def compute(start, end):
            if start + 1 >= end:
                return 0
            if memo[start][end] != -1:
                return memo[start][end]
            result = 0
            for split in range(start + 1, end):
                result = max(result,
                             balloons[start] * balloons[split] * balloons[end] +
                             compute(start, split) + compute(split, end))
            memo[start][end] = result
            return result

        return compute(0, size - 1)
