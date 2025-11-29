class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 5
        counts = [1] * 5
        for _ in range(n - 1):
            next_counts = [0] * 5
            next_counts[0] = (counts[1] + counts[2] + counts[4]) % MOD
            next_counts[1] = (counts[0] + counts[2]) % MOD
            next_counts[2] = (counts[1] + counts[3]) % MOD
            next_counts[3] = counts[2] % MOD
            next_counts[4] = (counts[2] + counts[3]) % MOD
            counts = next_counts
        return sum(counts) % MOD
