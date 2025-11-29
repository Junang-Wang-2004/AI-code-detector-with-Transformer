class Solution:
    def numberOfWays(self, num_people):
        mod = 10**9 + 7
        half = num_people // 2
        result = 1
        for k in range(1, half + 1):
            result = (result * (4 * k - 2) % mod * pow(k + 1, mod - 2, mod)) % mod
        return result
