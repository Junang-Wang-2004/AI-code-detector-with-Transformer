class Solution:
    def countOfArrays(self, n, m, k):
        MOD = 10**9 + 7
        cnt_even = m // 2
        cnt_odd = (m + 1) // 2
        ways_even = [0] * (k + 1)
        ways_odd = [0] * (k + 1)
        ways_even[0] = cnt_even
        ways_odd[0] = cnt_odd
        for pos in range(1, n):
            new_even = [0] * (k + 1)
            new_odd = [0] * (k + 1)
            for changes in range(k + 1):
                new_even[changes] = ways_even[changes] * cnt_even % MOD
                if changes > 0:
                    new_even[changes] = (new_even[changes] + ways_odd[changes - 1] * cnt_even) % MOD
                new_odd[changes] = ways_odd[changes] * cnt_odd % MOD
                if changes > 0:
                    new_odd[changes] = (new_odd[changes] + ways_even[changes - 1] * cnt_odd) % MOD
            ways_even = new_even
            ways_odd = new_odd
        return (ways_even[k] + ways_odd[k]) % MOD
