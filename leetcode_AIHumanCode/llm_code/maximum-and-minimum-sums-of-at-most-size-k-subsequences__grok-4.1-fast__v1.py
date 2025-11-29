class Solution(object):
    def minMaxSums(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)
        if n == 0 or k == 0:
            return 0
        arr = sorted(nums)
        r = k - 1
        ways = [0] * n
        ways[0] = 1
        cur_comb = 1 if r == 0 else 0
        def modinv(x):
            return pow(x, MOD - 2, MOD)
        for i in range(1, n):
            subtract = cur_comb if i - 1 >= r else 0
            ways[i] = (2 * ways[i - 1] - subtract + MOD) % MOD
            if i == r:
                cur_comb = 1
            elif i > r:
                cur_comb = cur_comb * (i * modinv(i - r)) % MOD
        total = 0
        for i in range(n):
            total = (total + arr[i] * ways[i] % MOD) % MOD
            total = (total + arr[i] * ways[n - 1 - i] % MOD) % MOD
        return total
