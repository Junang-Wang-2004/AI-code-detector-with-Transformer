class Solution:
    def countCompleteDayPairs(self, hours):
        MOD = 24
        counts = [0] * MOD
        total = 0
        for val in hours:
            r = val % MOD
            req = (MOD - r) % MOD
            total += counts[req]
            counts[r] += 1
        return total
