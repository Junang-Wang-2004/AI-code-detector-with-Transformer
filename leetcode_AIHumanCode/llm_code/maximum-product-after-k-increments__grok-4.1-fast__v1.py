class Solution:
    def maximumProduct(self, nums, k):
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + nums[i - 1]
        def check(length):
            if length == 0:
                return True
            target = nums[length - 1]
            cost = target * length - pref[length]
            return cost <= k
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        prefix_len = lo
        prefix_sum = pref[prefix_len]
        final_prefix_sum = prefix_sum + k
        quotient, remainder = divmod(final_prefix_sum, prefix_len)
        prefix_prod = pow(quotient, prefix_len - remainder, MOD) * pow(quotient + 1, remainder, MOD) % MOD
        result = prefix_prod
        for idx in range(prefix_len, n):
            result = result * nums[idx] % MOD
        return result
