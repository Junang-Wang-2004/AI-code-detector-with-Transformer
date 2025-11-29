class Solution:
    def getSum(self, nums):
        mod = 10**9 + 7
        def calc(delta):
            ends_count = {}
            ends_sum = {}
            res = 0
            for v in nums:
                p = v - delta
                prev_count = ends_count.get(p, 0)
                new_count = (prev_count + 1) % mod
                new_sum = (ends_sum.get(p, 0) + v * new_count) % mod
                ends_count[v] = (ends_count.get(v, 0) + new_count) % mod
                ends_sum[v] = (ends_sum.get(v, 0) + new_sum) % mod
                res = (res + new_sum) % mod
            return res
        up = calc(1)
        down = calc(-1)
        plain = sum(nums) % mod
        return (up + down - plain + mod) % mod
