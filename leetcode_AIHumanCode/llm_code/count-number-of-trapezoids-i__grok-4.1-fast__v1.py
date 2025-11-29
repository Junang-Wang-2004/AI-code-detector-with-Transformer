class Solution:
    def countTrapezoids(self, points):
        MOD = 10**9 + 7
        freq_map = {}
        for _, y_val in points:
            freq_map[y_val] = freq_map.get(y_val, 0) + 1
        group_sizes = list(freq_map.values())
        pair_counts = [sz * (sz - 1) // 2 % MOD for sz in group_sizes]
        sum_pairs = sum(pair_counts) % MOD
        sum_pair_squares = sum((pc * pc) % MOD for pc in pair_counts) % MOD
        diff = (sum_pairs * sum_pairs % MOD - sum_pair_squares + MOD) % MOD
        inv_two = pow(2, MOD - 2, MOD)
        return diff * inv_two % MOD
