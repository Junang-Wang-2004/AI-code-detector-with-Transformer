class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        sieve = [True] * n
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for multiple in range(i * i, n, i):
                    sieve[multiple] = False
        return sum(sieve)
