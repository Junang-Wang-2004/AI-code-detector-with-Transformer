class Solution(object):
    def findTargetSumWays(self, nums, S):
        total = sum(nums)
        if abs(S) > total or (S + total) % 2 != 0:
            return 0
        target = (S + total) // 2
        ways = [0] * (target + 1)
        ways[0] = 1
        for num in nums:
            for sum_val in range(target, num - 1, -1):
                ways[sum_val] += ways[sum_val - num]
        return ways[target]
