class Solution(object):
    def countOfPairs(self, nums):
        MOD = 10**9 + 7
        if not nums:
            return 0
        maxv = max(nums)
        curr_ways = [0] * (maxv + 1)
        for j in range(nums[0] + 1):
            curr_ways[j] = 1
        for k in range(1, len(nums)):
            step = max(0, nums[k] - nums[k - 1])
            next_ways = [0] * (maxv + 1)
            accum = 0
            for val in range(maxv + 1):
                if val >= step:
                    accum = (accum + curr_ways[val - step]) % MOD
                if val <= nums[k]:
                    next_ways[val] = accum
            curr_ways = next_ways
        result = 0
        for cnt in curr_ways:
            result = (result + cnt) % MOD
        return result
