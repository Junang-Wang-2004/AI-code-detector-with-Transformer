class Solution:
    def createSortedArray(self, instructions):
        MOD = 10**9 + 7
        if not instructions:
            return 0
        unique_vals = sorted(set(instructions))
        rank_map = {unique_vals[i]: i + 1 for i in range(len(unique_vals))}
        ft_size = len(unique_vals)
        ft_array = [0] * (ft_size + 1)
        def update_ft(idx, delta):
            while idx <= ft_size:
                ft_array[idx] += delta
                idx += idx & -idx
        def prefix_sum(idx):
            accum = 0
            while idx > 0:
                accum += ft_array[idx]
                idx -= idx & -idx
            return accum
        cost_sum = 0
        prev_count = 0
        for val in instructions:
            rnk = rank_map[val]
            lt_count = prefix_sum(rnk - 1)
            le_count = prefix_sum(rnk)
            gt_count = prev_count - le_count
            cost_sum = (cost_sum + min(lt_count, gt_count)) % MOD
            update_ft(rnk, 1)
            prev_count += 1
        return cost_sum
