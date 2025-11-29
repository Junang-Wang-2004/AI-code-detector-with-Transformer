class Solution(object):
    def countNumbers(self, l, r, b):
        MOD = 10**9 + 7
        MAXK = 100
        inv = [0] * (MAXK + 1)
        inv[1] = 1
        for i in range(2, MAXK + 1):
            inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
        def binom(n, k, mod):
            if k == 0:
                return 1
            if n < 0 or k < 0 or k > n:
                return 0
            res = 1
            for i in range(k):
                res = res * ((n - i) % mod) % mod
            for i in range(1, k + 1):
                res = res * inv[i] % mod
            return res
        def count_max(x, base, mod):
            if x < 0:
                return 0
            digits = []
            temp = x
            while temp:
                digits.append(temp % base)
                temp //= base
            digits.reverse()
            if not digits:
                digits = [0]
            nd = len(digits)
            ans = 0
            tight = True
            pd = 0
            for p in range(nd):
                u = digits[p]
                if p > 0 and pd > u:
                    tight = False
                    break
                sj = pd
                if sj < u:
                    rp = nd - p - 1
                    t_lo = base - (u - 1)
                    t_hi = base - sj
                    u_lo = t_lo + rp - 1
                    u_hi = t_hi + rp - 1
                    contrib = (binom(u_hi + 1, rp + 1, mod) - binom(u_lo, rp + 1, mod) + mod) % mod
                    ans = (ans + contrib) % mod
                pd = u
            if tight:
                ans = (ans + 1) % mod
            return ans
        return (count_max(int(r), b, MOD) - count_max(int(l) - 1, b, MOD) + MOD) % MOD
