class Solution:
    def minSubArrayLen(self, s, nums):
        length = len(nums)
        result = length + 1
        accum = 0
        begin = 0
        end = 0
        while end < length:
            accum += nums[end]
            while accum >= s:
                result = min(result, end - begin + 1)
                accum -= nums[begin]
                begin += 1
            end += 1
        return result if result <= length else 0
