class Solution(object):
    def magicalSum(self, m, k, nums):
        MOD = 10**9 + 7
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD
        invfact = [0] * (m + 1)
        invfact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m - 1, -1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % MOD

        def choose(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD

        CMAX = m + 1
        cur = [[[0 for _ in range(m + 1)] for _ in range(k + 1)] for _ in range(CMAX)]
        cur[0][0][m] = 1

        for val in nums:
            nxt = [[[0 for _ in range(m + 1)] for _ in range(k + 1)] for _ in range(CMAX)]
            for carry in range(CMAX):
                for bits in range(k + 1):
                    for left in range(m + 1):
                        contrib = cur[carry][bits][left]
                        if contrib == 0:
                            continue
                        power = 1
                        for take in range(left + 1):
                            sumdig = carry + take
                            newcarry = sumdig // 2
                            newbits = bits + (sumdig % 2)
                            if newbits > k:
                                continue
                            newleft = left - take
                            extra = contrib * power % MOD * choose(left, take) % MOD
                            nxt[newcarry][newbits][newleft] = (nxt[newcarry][newbits][newleft] + extra) % MOD
                            power = power * val % MOD
            cur = nxt

        result = 0
        for carry in range(CMAX):
            pc = bin(carry).count('1')
            target = k - pc
            if 0 <= target <= k:
                result = (result + cur[carry][target][0]) % MOD
        return result
