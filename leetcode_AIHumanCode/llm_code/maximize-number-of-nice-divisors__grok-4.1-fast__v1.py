class Solution:
    def maxNiceDivisors(self, total_factors):
        mod = 10**9 + 7
        num_threes = total_factors // 3
        remainder = total_factors % 3
        if remainder == 1 and num_threes > 0:
            num_threes -= 1
            return (pow(3, num_threes, mod) * 4) % mod
        elif remainder == 2:
            return (pow(3, num_threes, mod) * 2) % mod
        else:
            return pow(3, num_threes, mod) % mod
