# Time:  O(n)
# Space: O(n)
class Solution_TLE(object):
    def countPrimes(self, n):
        """
        """
        def linear_sieve_of_eratosthenes(n):
            primes = []
            spf = [-1]*(n+1)  # the smallest prime factor
            for i in range(2, n+1):
                if spf[i] == -1:
                    spf[i] = i
                    primes.append(i)
                for p in primes:
                    if i*p > n or p > spf[i]:
                        break
                    spf[i*p] = p
            return primes
    
        return len(linear_sieve_of_eratosthenes(n-1))
