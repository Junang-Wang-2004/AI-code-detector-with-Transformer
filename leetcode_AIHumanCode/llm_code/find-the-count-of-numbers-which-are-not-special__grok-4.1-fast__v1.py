import bisect

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]

MAX_R = 10**9
sqrt_limit = int(MAX_R ** 0.5)
all_primes = sieve(sqrt_limit)
prime_squares = [p * p for p in all_primes]

class Solution(object):
    def nonSpecialCount(self, l, r):
        num_special = bisect.bisect_right(prime_squares, r) - bisect.bisect_left(prime_squares, l)
        return r - l + 1 - num_special
