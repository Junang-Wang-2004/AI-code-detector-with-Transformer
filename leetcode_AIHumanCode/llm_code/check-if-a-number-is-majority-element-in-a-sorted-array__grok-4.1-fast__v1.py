class Solution:
    def isMajorityElement(self, nums, target):
        def lower(nums, val):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < val:
                    left = mid + 1
                else:
                    right = mid
            return left

        def upper(nums, val):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= val:
                    left = mid + 1
                else:
                    right = mid
            return left

        occurrences = upper(nums, target) - lower(nums, target)
        return occurrences * 2 > len(nums)
