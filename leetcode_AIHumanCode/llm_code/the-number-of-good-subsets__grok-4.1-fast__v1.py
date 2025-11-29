import collections

class Solution:
    def numberOfGoodSubsets(self, nums):
        MOD = 10**9 + 7
        if not nums:
            return 0
        max_val = max(nums)
        sieve = [True] * (max_val + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(max_val**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, max_val + 1, i):
                    sieve[j] = False
        primes_list = [i for i in range(2, max_val + 1) if sieve[i]]
        state_size = 1 << len(primes_list)
        freq_map = collections.Counter(nums)
        count_ones = freq_map.pop(1, 0)
        subset_ways = [0] * state_size
        subset_ways[0] = 1
        for value, count_val in list(freq_map.items()):
            current_mask = 0
            valid_num = True
            for prime_idx, prime_val in enumerate(primes_list):
                if value % (prime_val * prime_val) == 0:
                    valid_num = False
                    break
                if value % prime_val == 0:
                    current_mask |= (1 << prime_idx)
            if not valid_num:
                continue
            for current_state in range(state_size):
                if (current_state & current_mask) == 0:
                    new_mask = current_state | current_mask
                    subset_ways[new_mask] = (subset_ways[new_mask] + subset_ways[current_state] * count_val) % MOD
        total_combos = sum(subset_ways) % MOD
        result = (pow(2, count_ones, MOD) * total_combos - 1) % MOD
        return result
