class Solution:
    def nthSuperUglyNumber(self, n, primes):
        m = len(primes)
        seq = [0] * n
        seq[0] = 1
        pos = [0] * m
        for i in range(1, n):
            curr_min = min(primes[j] * seq[pos[j]] for j in range(m))
            seq[i] = curr_min
            for j in range(m):
                if primes[j] * seq[pos[j]] == curr_min:
                    pos[j] += 1
        return seq[-1]
