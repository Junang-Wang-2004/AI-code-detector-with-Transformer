class Solution:
    def findSmallestInteger(self, nums, value):
        freq = [0] * value
        for x in nums:
            freq[x % value] += 1
        return min(freq[i] * value + i for i in range(value))
