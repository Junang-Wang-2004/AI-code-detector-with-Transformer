class Solution:
    def largestDivisibleSubset(self, numbers):
        if not numbers:
            return []
        numbers.sort()
        n = len(numbers)
        chains = [[numbers[i]] for i in range(n)]
        for i in range(n):
            for j in range(i):
                if numbers[i] % numbers[j] == 0 and len(chains[i]) < len(chains[j]) + 1:
                    chains[i] = chains[j][:] + [numbers[i]]
        return max(chains, key=len)
