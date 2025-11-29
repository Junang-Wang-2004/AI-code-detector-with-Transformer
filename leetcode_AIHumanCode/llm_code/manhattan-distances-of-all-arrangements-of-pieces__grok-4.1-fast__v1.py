MOD = 10**9 + 7

class Solution:
    def distanceSum(self, height, width, count):
        grid_size = height * width
        if count < 2:
            return 0

        def comb(N, K):
            if K < 0 or K > N:
                return 0
            fact_N = 1
            for i in range(2, N + 1):
                fact_N = fact_N * i % MOD
            fact_K = 1
            for i in range(2, K + 1):
                fact_K = fact_K * i % MOD
            fact_NK = 1
            for i in range(2, N - K + 1):
                fact_NK = fact_NK * i % MOD
            inv_K = pow(fact_K, MOD - 2, MOD)
            inv_NK = pow(fact_NK, MOD - 2, MOD)
            return fact_N * inv_K % MOD * inv_NK % MOD

        ways = comb(grid_size - 2, count - 2)

        def line_pairs(size):
            return size * (size - 1) * (size + 1) // 6

        row_dists = line_pairs(height) * width * width
        col_dists = line_pairs(width) * height * height
        pair_sums = row_dists + col_dists
        return pair_sums * ways % MOD
