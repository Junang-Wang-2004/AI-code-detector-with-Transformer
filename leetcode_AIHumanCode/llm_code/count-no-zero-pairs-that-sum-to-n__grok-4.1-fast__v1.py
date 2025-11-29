class Solution(object):
    def countNoZeroPairs(self, n):
        digits = []
        m = n
        while m:
            digits.append(m % 10)
            m //= 10
        dp = [0] * 8
        dp[0] = 1
        first = True
        for d in digits:
            new_dp = [0] * 8
            lo = 1 if first else 0
            first = False
            for s in range(8):
                if dp[s] == 0:
                    continue
                c = s >> 2
                af = (s >> 1) & 1
                bf = s & 1
                alo = lo if af == 0 else 0
                ahi = 9 if af == 0 else 0
                for da in range(alo, ahi + 1):
                    naf = 1 if af or da == 0 else 0
                    blo = lo if bf == 0 else 0
                    bhi = 9 if bf == 0 else 0
                    for db in range(blo, bhi + 1):
                        nbf = 1 if bf or db == 0 else 0
                        tot = c + da + db
                        if tot % 10 == d:
                            nc = tot // 10
                            ns = (nc << 2) | (naf << 1) | nbf
                            new_dp[ns] += dp[s]
            dp = new_dp
        return sum(dp[:4])
