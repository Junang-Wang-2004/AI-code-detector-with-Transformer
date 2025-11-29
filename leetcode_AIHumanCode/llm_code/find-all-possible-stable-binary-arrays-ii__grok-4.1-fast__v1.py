class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7
        totals = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]
        ways = [[[[0] * (limit + 1) for _ in range(2)] for _ in range(one + 1)] for _ in range(zero + 1)]
        totals[0][0][0] = 1
        totals[0][0][1] = 1
        for a in range(zero + 1):
            for b in range(one + 1):
                if a == 0 and b == 0:
                    continue
                if a > 0:
                    ways[a][b][0][1] = totals[a - 1][b][1]
                    for k in range(2, limit + 1):
                        ways[a][b][0][k] = ways[a - 1][b][0][k - 1]
                if b > 0:
                    ways[a][b][1][1] = totals[a][b - 1][0]
                    for k in range(2, limit + 1):
                        ways[a][b][1][k] = ways[a][b - 1][1][k - 1]
                totals[a][b][0] = sum(ways[a][b][0][1:]) % MOD
                totals[a][b][1] = sum(ways[a][b][1][1:]) % MOD
        return (totals[zero][one][0] + totals[zero][one][1]) % MOD
