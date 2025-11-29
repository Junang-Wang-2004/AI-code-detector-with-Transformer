class Solution:
    def sumOfLargestPrimes(self, s):
        def check_prime(val):
            if val <= 1:
                return False
            if val <= 3:
                return True
            if val % 2 == 0 or val % 3 == 0:
                return False
            idx = 5
            while idx * idx <= val:
                if val % idx == 0 or val % (idx + 2) == 0:
                    return False
                idx += 6
            return True
        
        prime_candidates = set()
        n = len(s)
        for length in range(1, n + 1):
            for start_pos in range(n - length + 1):
                substr = s[start_pos:start_pos + length]
                numeric_val = int(substr)
                if numeric_val > 1 and check_prime(numeric_val):
                    prime_candidates.add(numeric_val)
        
        sorted_primes = sorted(prime_candidates, reverse=True)
        k = min(3, len(sorted_primes))
        return sum(sorted_primes[:k])
