class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        cnt = collections.Counter(s)
        if len(cnt) < k:
            return 0
        vals = sorted(cnt.values(), reverse=True)
        m_val = vals[k - 1]
        num_greater = 0
        while num_greater < k and vals[num_greater] > m_val:
            num_greater += 1
        num_needed = k - num_greater
        num_equal = sum(1 for v in vals[num_greater:] if v == m_val)
        if num_needed > num_equal:
            return 0
        prod = 1
        for i in range(num_greater):
            prod = (prod * vals[i]) % MOD
        prod = (prod * pow(m_val, num_needed, MOD)) % MOD
        comb = 1
        for i in range(1, num_needed + 1):
            comb = (comb * (num_equal - i + 1)) % MOD
            comb = (comb * pow(i, MOD - 2, MOD)) % MOD
        return (prod * comb) % MOD
