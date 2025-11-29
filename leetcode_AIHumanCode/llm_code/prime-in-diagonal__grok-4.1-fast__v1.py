MAX_N = 4_000_001
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX_N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False

class Solution:
    def diagonalPrime(self, nums):
        size = len(nums)
        maximum_prime = 0
        for row in range(size):
            for position in (row, size - 1 - row):
                candidate = nums[row][position]
                if 2 <= candidate < MAX_N and is_prime[candidate]:
                    maximum_prime = max(maximum_prime, candidate)
        return maximum_prime
