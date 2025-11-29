class Solution:
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            pivot = (start + end) // 2
            if nums[pivot] > nums[end]:
                start = pivot + 1
            else:
                end = pivot
        return nums[start]
