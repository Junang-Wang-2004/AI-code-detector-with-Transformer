class Solution:
    def kInversePairs(self, n, k):
        MOD = 10**9 + 7
        ways = [0] * (k + 1)
        ways[0] = 1
        for length in range(1, n + 1):
            prefix = [0] * (k + 2)
            for idx in range(k + 1):
                prefix[idx + 1] = (prefix[idx] + ways[idx]) % MOD
            max_add = length - 1
            next_ways = [0] * (k + 1)
            for target in range(k + 1):
                start = max(0, target - max_add)
                next_ways[target] = (prefix[target + 1] - prefix[start] + MOD) % MOD
            ways = next_ways
        return ways[k]
