class Solution(object):
    def numPrimeArrangements(self, n):
        MOD = 10**9 + 7
        facts = [1] * (n + 1)
        for i in range(2, n + 1):
            facts[i] = facts[i - 1] * i % MOD
        
        def count_primes(limit):
            if limit < 2:
                return 0
            marks = [True] * (limit + 1)
            marks[0] = marks[1] = False
            for k in range(2, int(limit ** 0.5) + 1):
                if marks[k]:
                    for m in range(k * k, limit + 1, k):
                        marks[m] = False
            return sum(marks)
        
        primes = count_primes(n)
        return facts[primes] * facts[n - primes] % MOD
