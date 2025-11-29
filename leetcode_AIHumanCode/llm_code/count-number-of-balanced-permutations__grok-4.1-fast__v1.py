class Solution(object):
    def countBalancedPermutations(self, num):
        MOD = 10**9 + 7
        n = len(num)
        total_sum = sum(int(d) for d in num)
        if total_sum % 2 != 0:
            return 0
        target = total_sum // 2
        group_a = n // 2
        group_b = n - group_a
        freq = [0] * 10
        for char in num:
            freq[int(char)] += 1
        
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        def inverse(x):
            return pow(x, MOD - 2, MOD)
        
        inv_fact = [inverse(fact[i]) for i in range(n + 1)]
        
        def choose(n_val, k_val):
            if k_val < 0 or k_val > n_val:
                return 0
            return fact[n_val] * inv_fact[k_val] % MOD * inv_fact[n_val - k_val] % MOD
        
        prev_dp = [[0] * (group_a + 1) for _ in range(target + 1)]
        prev_dp[0][0] = 1
        
        for d in range(10):
            if freq[d] == 0:
                continue
            curr_dp = [[0] * (group_a + 1) for _ in range(target + 1)]
            for s in range(target + 1):
                for p in range(group_a + 1):
                    if prev_dp[s][p] == 0:
                        continue
                    for c in range(freq[d] + 1):
                        ns = s + c * d
                        np = p + c
                        if ns > target or np > group_a:
                            break
                        curr_dp[ns][np] = (curr_dp[ns][np] + prev_dp[s][p] * choose(freq[d], c)) % MOD
            prev_dp = curr_dp
        
        result = prev_dp[target][group_a]
        result = result * fact[group_a] % MOD
        result = result * fact[group_b] % MOD
        for f in freq:
            result = result * inv_fact[f] % MOD
        return result
