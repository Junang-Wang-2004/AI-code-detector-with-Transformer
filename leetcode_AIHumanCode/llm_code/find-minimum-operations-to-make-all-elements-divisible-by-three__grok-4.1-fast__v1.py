class Solution:
    def minimumOperations(self, nums):
        total = 0
        for num in nums:
            r = num % 3
            if r > 0:
                total += 1
        return total
