import sys
sys.setrecursionlimit(10**6)

class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        MAXN = 1005
        factorial = [1] * MAXN
        for i in range(1, MAXN):
            factorial[i] = factorial[i-1] * i % MOD
        def mod_inverse(a):
            return pow(a, MOD - 2, MOD)
        def binomial(n, k):
            if k < 0 or k > n:
                return 0
            return factorial[n] * mod_inverse(factorial[k]) % MOD * mod_inverse(factorial[n - k]) % MOD
        def compute_ways(arr):
            size = len(arr)
            if size <= 2:
                return 1
            root = arr[0]
            left_arr = []
            right_arr = []
            for num in arr[1:]:
                if num < root:
                    left_arr.append(num)
                else:
                    right_arr.append(num)
            interleave_ways = binomial(size - 1, len(left_arr))
            left_ways = compute_ways(left_arr)
            right_ways = compute_ways(right_arr)
            return interleave_ways * left_ways % MOD * right_ways % MOD
        total = compute_ways(nums)
        return (total - 1) % MOD
