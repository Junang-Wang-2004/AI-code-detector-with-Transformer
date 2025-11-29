from math import gcd

class Solution:
    def maxScore(self, nums):
        n = len(nums)
        N = 1 << n
        memo = [0] * N
        for mask in range(N):
            bits = bin(mask).count('1')
            if bits % 2 != 0 or bits == 0:
                continue
            half = bits // 2
            for i in range(n):
                if (mask & (1 << i)) == 0:
                    continue
                for j in range(i + 1, n):
                    if (mask & (1 << j)) == 0:
                        continue
                    prev = mask ^ (1 << i) ^ (1 << j)
                    val = half * gcd(nums[i], nums[j]) + memo[prev]
                    if val > memo[mask]:
                        memo[mask] = val
        return memo[N - 1]
