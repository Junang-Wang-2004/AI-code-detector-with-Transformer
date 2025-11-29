class Solution:
    def makeStringSorted(self, s):
        MOD = 10**9 + 7
        n = len(s)
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        invfact = [0] * (n + 1)
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % MOD
        rem = [0] * 26
        for c in s:
            rem[ord(c) - ord('a')] += 1
        denom_inv = 1
        for j in range(26):
            denom_inv = denom_inv * invfact[rem[j]] % MOD
        total = 0
        length = n
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            sm = 0
            for j in range(idx):
                sm += rem[j]
            if sm:
                suffix_ways = fact[length] * denom_inv % MOD
                add = sm * suffix_ways % MOD * pow(length, MOD - 2, MOD) % MOD
                total = (total + add) % MOD
            prev = rem[idx]
            rem[idx] -= 1
            denom_inv = denom_inv * fact[prev] % MOD * invfact[prev - 1] % MOD
            length -= 1
        return total
