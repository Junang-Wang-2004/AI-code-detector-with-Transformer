class Solution:
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7
        tot = n + k - 1
        sel = 2 * k
        if sel > tot:
            return 0
        alt = tot - sel
        if sel > alt:
            sel = alt
        ans = 1
        for j in range(1, sel + 1):
            ans = ans * (tot - j + 1) // j
        return ans % MOD
