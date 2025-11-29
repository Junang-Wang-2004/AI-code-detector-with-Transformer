class Solution:
    def numberOfWays(self, corridor):
        MOD = 10**9 + 7
        pos = [i for i, c in enumerate(corridor) if c == 'S']
        n = len(pos)
        if n == 0 or n % 2 != 0:
            return 0
        ans = 1
        for idx in range(1, n // 2):
            ans = ans * (pos[2 * idx] - pos[2 * idx - 1]) % MOD
        return ans
