import collections

def get_primes(limit):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if flags[i]:
            for j in range(i * i, limit + 1, i):
                flags[j] = False
    return {i for i in range(2, limit + 1) if flags[i]}

MAX_FREQ = 100
prime_set = get_primes(MAX_FREQ)

class Solution(object):
    def checkPrimeFrequency(self, nums):
        frequency = collections.Counter(nums)
        return any(freq in prime_set for freq in frequency.values())
