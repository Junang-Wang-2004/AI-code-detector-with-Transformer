def compute_smallest_prime_factors(limit):
    smallest_factors = list(range(limit + 1))
    for i in range(2, int(limit ** 0.5) + 1):
        if smallest_factors[i] == i:
            for j in range(i * i, limit + 1, i):
                if smallest_factors[j] == j:
                    smallest_factors[j] = i
    return smallest_factors

MAX_VALUE = 10**6 + 10
SMALL_PRIME_FACTORS = compute_smallest_prime_factors(MAX_VALUE)

class Solution(object):
    def minOperations(self, nums):
        if not nums:
            return 0
        operations = 0
        required_max = nums[-1]
        for position in range(len(nums) - 2, -1, -1):
            current = nums[position]
            if current <= required_max:
                required_max = current
            else:
                candidate = SMALL_PRIME_FACTORS[current]
                if candidate > required_max:
                    return -1
                required_max = candidate
                operations += 1
        return operations
