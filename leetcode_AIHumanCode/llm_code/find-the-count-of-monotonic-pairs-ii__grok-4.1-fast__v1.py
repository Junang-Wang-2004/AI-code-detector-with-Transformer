class Solution:
    def countOfPairs(self, nums):
        MOD = 10**9 + 7
        if not nums:
            return 0
        mx = max(nums)
        ways = [0] * (mx + 1)
        for v in range(nums[0] + 1):
            ways[v] = 1
        for pos in range(1, len(nums)):
            mind = max(nums[pos] - nums[pos - 1], 0)
            psum = [0] * (mx + 2)
            for k in range(1, mx + 2):
                psum[k] = (psum[k - 1] + ways[k - 1]) % MOD
            nxt_ways = [0] * (mx + 1)
            for val in range(nums[pos] + 1):
                prv_max = val - mind
                if prv_max >= 0:
                    nxt_ways[val] = psum[prv_max + 1]
            ways = nxt_ways
        return sum(ways) % MOD
