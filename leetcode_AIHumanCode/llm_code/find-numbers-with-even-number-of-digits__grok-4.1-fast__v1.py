class Solution:
    def findNumbers(self, nums):
        total = 0
        for value in nums:
            if (10 <= value < 100) or (1000 <= value < 10000) or (value >= 100000):
                total += 1
        return total
