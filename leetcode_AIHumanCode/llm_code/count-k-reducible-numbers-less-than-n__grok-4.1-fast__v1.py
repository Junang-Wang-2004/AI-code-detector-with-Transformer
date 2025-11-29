class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        cnt = [0] * n
        for i in range(2, n):
            pc = 0
            tmp = i
            while tmp:
                pc += tmp & 1
                tmp >>= 1
            cnt[i] = cnt[pc] + 1
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        invfact = [0] * (n + 1)
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % MOD
        def comb(m, c):
            if c < 0 or c > m: return 0
            return fact[m] * invfact[c] % MOD * invfact[m - c] % MOD
        ans = 0
        prev = 0
        for i in range(n):
            if s[i] == '1':
                rem = n - i - 1
                for c in range(rem + 1):
                    tot = prev + c
                    if tot < n and cnt[tot] < k:
                        ans = (ans + comb(rem, c)) % MOD
                prev += 1
        return (ans - 1) % MOD
