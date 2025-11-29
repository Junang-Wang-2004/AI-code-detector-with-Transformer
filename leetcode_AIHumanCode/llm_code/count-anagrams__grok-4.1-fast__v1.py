import collections

class Solution(object):
    def countAnagrams(self, s):
        MOD = 10**9 + 7
        n = len(s)
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i % MOD
        terms = s.split()
        total = 1
        for term in terms:
            length = len(term)
            frequencies = collections.Counter(term)
            ways = factorial[length]
            for count in frequencies.values():
                ways = ways * pow(factorial[count], MOD - 2, MOD) % MOD
            total = total * ways % MOD
        return total
