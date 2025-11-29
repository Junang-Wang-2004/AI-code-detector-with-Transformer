class Solution:
    def countDistinct(self, nums, k, p):
        n = len(nums)
        prefix_zeros = [0] * (n + 1)
        for i in range(n):
            prefix_zeros[i + 1] = prefix_zeros[i] + (nums[i] % p == 0)
        MOD = 10**9 + 7
        BASE = 131
        prefix_hash = [0] * (n + 1)
        base_pow = [1] * (n + 1)
        for i in range(n):
            prefix_hash[i + 1] = (prefix_hash[i] * BASE + nums[i]) % MOD
            base_pow[i + 1] = base_pow[i] * BASE % MOD
        def get_subarray_hash(l, r):
            sz = r - l + 1
            h = (prefix_hash[r + 1] - prefix_hash[l] * base_pow[sz] % MOD + MOD) % MOD
            return h
        ans = 0
        for sz in range(1, n + 1):
            hashes = set()
            for begin in range(n - sz + 1):
                fin = begin + sz - 1
                zeros_cnt = prefix_zeros[fin + 1] - prefix_zeros[begin]
                if zeros_cnt <= k:
                    hashes.add(get_subarray_hash(begin, fin))
            ans += len(hashes)
        return ans
