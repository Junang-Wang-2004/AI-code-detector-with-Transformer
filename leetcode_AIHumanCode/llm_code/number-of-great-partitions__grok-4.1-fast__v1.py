class Solution:
    def countPartitions(self, nums, k):
        mod = 10**9 + 7
        total = sum(nums)
        if total < 2 * k:
            return 0
        ways = [1] + [0] * (k - 1)
        for num in nums:
            new_ways = [0] * k
            for j in range(k):
                new_ways[j] = ways[j]
                if j >= num:
                    new_ways[j] = (new_ways[j] + ways[j - num]) % mod
            ways = new_ways
        small = sum(ways) % mod
        all_sets = pow(2, len(nums), mod)
        return (all_sets - 2 * small) % mod
