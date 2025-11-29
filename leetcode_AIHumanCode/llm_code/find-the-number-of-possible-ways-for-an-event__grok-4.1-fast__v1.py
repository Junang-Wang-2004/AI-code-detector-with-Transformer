MOD = 10**9 + 7
MAX_VAL = 1005
binoms = [[0] * MAX_VAL for _ in range(MAX_VAL)]
surjections = [[0] * MAX_VAL for _ in range(MAX_VAL)]
powers = [[1] * MAX_VAL for _ in range(MAX_VAL)]
binoms[0][0] = 1
for row in range(1, MAX_VAL):
    binoms[row][0] = 1
    for col in range(1, row + 1):
        if col < MAX_VAL:
            binoms[row][col] = (binoms[row - 1][col] + binoms[row - 1][col - 1]) % MOD
surjections[0][0] = 1
for row in range(1, MAX_VAL):
    for col in range(1, row + 1):
        if col < MAX_VAL:
            term1 = col * surjections[row - 1][col] % MOD
            term2 = col * surjections[row - 1][col - 1] % MOD
            surjections[row][col] = (term1 + term2) % MOD
for base in range(1, MAX_VAL):
    for exp in range(1, MAX_VAL):
        powers[base][exp] = powers[base][exp - 1] * base % MOD

class Solution(object):
    def numberOfWays(self, n, x, y):
        result = 0
        upper = min(n, x)
        for idx in range(1, upper + 1):
            contrib = binoms[x][idx] * surjections[n][idx] % MOD
            contrib = contrib * powers[y][idx] % MOD
            result = (result + contrib) % MOD
        return result
