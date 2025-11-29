import collections
import math

LIMIT = 1000000
is_prime = [True] * LIMIT
is_prime[0] = is_prime[1] = False
for i in range(2, math.isqrt(LIMIT) + 1):
    if is_prime[i]:
        for j in range(i * i, LIMIT, i):
            is_prime[j] = False

class Solution:
    def mostFrequentPrime(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        freq = collections.Counter()
        for sr in range(rows):
            for sc in range(cols):
                for dr, dc in dirs:
                    num = 0
                    r = sr
                    c = sc
                    while 0 <= r < rows and 0 <= c < cols:
                        num = num * 10 + mat[r][c]
                        if num > 10 and num < LIMIT and is_prime[num]:
                            freq[num] += 1
                        r += dr
                        c += dc
        return max(freq, key=lambda p: (freq[p], p)) if freq else -1
