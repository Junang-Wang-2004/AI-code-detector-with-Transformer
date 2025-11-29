class Solution(object):
    def getSum(self, nums):
        MOD = 10**9 + 7
        def process(delta):
            accum = 0
            seg_len = 0
            weighted = 0
            for idx in range(len(nums)):
                if seg_len == 0 or nums[idx] - nums[idx - 1] != delta:
                    seg_len = 1
                    weighted = (nums[idx] * 1) % MOD
                    accum = (accum + weighted) % MOD
                else:
                    seg_len += 1
                    weighted = (weighted + nums[idx] * seg_len % MOD) % MOD
                    accum = (accum + weighted) % MOD
            return accum
        all_sum = 0
        for val in nums:
            all_sum = (all_sum + val) % MOD
        c1 = process(1)
        c2 = process(-1)
        return (c1 + c2 - all_sum + MOD) % MOD
