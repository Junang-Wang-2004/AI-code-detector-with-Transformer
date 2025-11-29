class Solution(object):
    def distributeCookies(self, piles, num_kids):
        n = len(piles)
        full_mask = (1 << n) - 1
        subset_sum = [0] * (1 << n)
        for i in range(n):
            mask_bit = 1 << i
            for state in range(1 << n):
                if state & mask_bit:
                    subset_sum[state] += piles[i]
        INF = float('inf')
        memo = [[INF] * (1 << n) for _ in range(num_kids + 1)]
        memo[0][0] = 0
        for child in range(1, num_kids + 1):
            for state in range(1 << n):
                subset = state
                while subset:
                    child_load = subset_sum[subset]
                    prev_state = state ^ subset
                    prev_val = memo[child - 1][prev_state]
                    memo[child][state] = min(memo[child][state], max(child_load, prev_val))
                    subset = (subset - 1) & state
        return memo[num_kids][full_mask]
