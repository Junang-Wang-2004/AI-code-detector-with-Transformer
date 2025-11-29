class Solution:
    def getConcatenation(self, nums):
        result = []
        n = len(nums)
        for i in range(n):
            result.append(nums[i])
        for i in range(n):
            result.append(nums[i])
        return result
