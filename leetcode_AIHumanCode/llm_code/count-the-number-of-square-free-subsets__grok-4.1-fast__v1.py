import collections

class Solution(object):
    def squareFreeSubsets(self, nums):
        MOD = 10**9 + 7
        if not nums:
            return 0
        max_val = max(nums)
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        primes = [i for i in range(2, max_val + 1) if spf[i] == i]
        prime_idx = {p: i for i, p in enumerate(primes)}
        cnt = collections.Counter(nums)
        num_ones = cnt[1]
        valid_items = []
        for val, freq in cnt.items():
            if val == 1:
                continue
            cur = val
            mask = 0
            is_square_free = True
            while cur > 1:
                p = spf[cur]
                bit = 1 << prime_idx[p]
                mask |= bit
                cur //= p
                if cur % p == 0:
                    is_square_free = False
                    break
            if is_square_free:
                valid_items.append((mask, freq))
        num_primes = len(primes)
        full_mask = (1 << num_primes) - 1
        dp = [1] * (1 << num_primes)
        for item_mask, freq in valid_items:
            new_dp = [0] * (1 << num_primes)
            for state in range(1 << num_primes):
                if dp[state] == 0:
                    continue
                new_dp[state] = (new_dp[state] + dp[state]) % MOD
                if (state & item_mask) == 0:
                    new_state = state | item_mask
                    new_dp[new_state] = (new_dp[new_state] + freq * dp[state]) % MOD
            dp = new_dp
        ways = (dp[full_mask] * pow(2, num_ones, MOD) - 1) % MOD
        return ways
