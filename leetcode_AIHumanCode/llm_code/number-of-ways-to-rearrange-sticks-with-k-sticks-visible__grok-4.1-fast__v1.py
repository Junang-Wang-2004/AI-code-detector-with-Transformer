class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        ways = [0] * (k + 1)
        ways[1] = 1
        for length in range(2, n + 1):
            factor = length - 1
            for visible in range(k, 0, -1):
                ways[visible] = (ways[visible - 1] + factor * ways[visible]) % MOD
        return ways[k]
