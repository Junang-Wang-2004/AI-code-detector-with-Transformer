# Time:  O(n * k)
# Space: O(n + k)
# TLE due to the last test case, but it passess and performs the best in C++.
class Solution4(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        """
        uglies = [0] * n
        uglies[0] = 1
        ugly_by_prime = list(primes)
        idx = [0] * len(primes)

        for i in range(1, n):
            uglies[i] = min(ugly_by_prime)
            for k in range(len(primes)):
                if uglies[i] == ugly_by_prime[k]:
                    idx[k] += 1
                    ugly_by_prime[k] = primes[k] * uglies[idx[k]]

        return uglies[-1]

