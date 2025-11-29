class Solution(object):
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        end = -1
        maximum = float('-inf')
        for i in range(n):
            if nums[i] < maximum:
                end = i
            maximum = max(maximum, nums[i])
        start = n
        minimum = float('inf')
        for i in range(n - 1, -1, -1):
            if nums[i] > minimum:
                start = i
            minimum = min(minimum, nums[i])
        return 0 if start > end else end - start + 1
