class Solution:
    def countGoodSubsequences(self, s):
        MOD = 10**9 + 7
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        maxf = max(freq)
        fact = [1] * (maxf + 1)
        for i in range(1, maxf + 1):
            fact[i] = fact[i - 1] * i % MOD
        invfact = [pow(fact[i], MOD - 2, MOD) for i in range(maxf + 1)]
        def choose(n, k):
            if k < 0 or k > n:
                return 0
            return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD
        total = 0
        for k in range(1, maxf + 1):
            ways = 1
            for f in freq:
                ways = ways * (1 + choose(f, k)) % MOD
            total = (total + ways - 1) % MOD
        return total
