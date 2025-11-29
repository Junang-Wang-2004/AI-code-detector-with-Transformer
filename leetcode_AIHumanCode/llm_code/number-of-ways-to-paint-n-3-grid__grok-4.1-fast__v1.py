class Solution(object):
    def numOfWays(self, n):
        MOD = 10**9 + 7
        
        def mult(X, Y):
            return [
                [(X[0][0] * Y[0][0] + X[0][1] * Y[1][0]) % MOD, (X[0][0] * Y[0][1] + X[0][1] * Y[1][1]) % MOD],
                [(X[1][0] * Y[0][0] + X[1][1] * Y[1][0]) % MOD, (X[1][0] * Y[0][1] + X[1][1] * Y[1][1]) % MOD]
            ]
        
        def power(base, k):
            ans = [[1, 0], [0, 1]]
            while k > 0:
                if k & 1:
                    ans = mult(ans, base)
                base = mult(base, base)
                k >>= 1
            return ans
        
        M = [[3, 2], [2, 2]]
        if n == 0:
            return 0
        P = power(M, n - 1)
        res0 = (6 * P[0][0] + 6 * P[1][0]) % MOD
        res1 = (6 * P[0][1] + 6 * P[1][1]) % MOD
        return (res0 + res1) % MOD
