class Solution(object):
    def primeSubOperation(self, nums):
        def generate_primes(limit):
            factors = [True] * (limit + 1)
            factors[0] = factors[1] = False
            for num in range(2, int(limit ** 0.5) + 1):
                if factors[num]:
                    for multiple in range(num * num, limit + 1, num):
                        factors[multiple] = False
            return [num for num in range(2, limit + 1) if factors[num]]

        all_primes = generate_primes(1000)
        minimum = 0
        for value in nums:
            diff = value - minimum
            subtract = 0
            for candidate in reversed(all_primes):
                if candidate < diff:
                    subtract = candidate
                    break
            updated = value - subtract
            if updated <= minimum:
                return False
            minimum = updated
        return True
