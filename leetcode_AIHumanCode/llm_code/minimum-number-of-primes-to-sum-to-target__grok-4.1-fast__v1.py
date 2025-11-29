class Solution(object):
    def minNumberOfPrimes(self, n, m):
        if n == 0:
            return 0
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        prime_list = [i for i in range(2, n + 1) if sieve[i]][:m]
        INF = float('inf')
        ways = [INF] * (n + 1)
        ways[0] = 0
        for p in prime_list:
            for s in range(p, n + 1):
                ways[s] = min(ways[s], ways[s - p] + 1)
        return ways[n] if ways[n] != INF else -1
