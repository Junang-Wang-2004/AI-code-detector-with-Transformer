class Solution:
    def searchRange(self, nums, target):
        size = len(nums)
        low, high = 0, size
        while low < high:
            pivot = (low + high) // 2
            if nums[pivot] < target:
                low = pivot + 1
            else:
                high = pivot
        first = low
        if first == size or nums[first] != target:
            return [-1, -1]
        low, high = 0, size
        while low < high:
            pivot = (low + high) // 2
            if nums[pivot] <= target:
                low = pivot + 1
            else:
                high = pivot
        last = low - 1
        return [first, last]
