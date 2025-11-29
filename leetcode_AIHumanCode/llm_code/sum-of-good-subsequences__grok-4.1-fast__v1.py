class Solution(object):
    def sumOfGoodSubsequences(self, nums):
        MOD = 10**9 + 7
        end_ways = {}
        prefix_sums = {}
        for val in nums:
            neigh_l = end_ways.get(val - 1, 0)
            neigh_r = end_ways.get(val + 1, 0)
            append_cnt = (neigh_l + neigh_r + 1) % MOD
            end_ways[val] = (end_ways.get(val, 0) + append_cnt) % MOD
            sum_l = prefix_sums.get(val - 1, 0)
            sum_r = prefix_sums.get(val + 1, 0)
            incr = (sum_l + sum_r + val * append_cnt % MOD) % MOD
            prefix_sums[val] = (prefix_sums.get(val, 0) + incr) % MOD
        result = 0
        for s in prefix_sums.values():
            result = (result + s) % MOD
        return result
