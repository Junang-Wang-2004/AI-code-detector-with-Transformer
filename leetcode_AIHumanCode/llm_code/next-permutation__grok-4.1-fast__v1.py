class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            self.reverse_range(nums, 0, n - 1)
            return
        j = n - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        self.reverse_range(nums, i + 1, n - 1)

    def reverse_range(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
