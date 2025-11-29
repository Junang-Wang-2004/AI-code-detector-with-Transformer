class Solution:
    def distinctPrimeFactors(self, nums):
        unique_primes = set()
        candidates = set(nums)
        for val in candidates:
            if val < 2:
                continue
            divisor = 2
            while divisor * divisor <= val:
                while val % divisor == 0:
                    unique_primes.add(divisor)
                    val //= divisor
                divisor += 1
            if val > 1:
                unique_primes.add(val)
        return len(unique_primes)
