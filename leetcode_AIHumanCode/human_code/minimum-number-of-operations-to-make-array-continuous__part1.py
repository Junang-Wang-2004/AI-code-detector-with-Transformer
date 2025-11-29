# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def minOperations(self, nums):
        """
        """
        def unique(nums):
            left = 0
            for right in range(1, len(nums)):
                if nums[left] != nums[right]:
                    left += 1
                    nums[left] = nums[right]
            return left

        def erase(nums, i):
            while len(nums) > i+1:
                nums.pop()

        n = len(nums)
        nums.sort()
        erase(nums, unique(nums))
        result = l = 0
        for i in range(len(nums)):
            if nums[i] <= nums[i-l]+n-1:
                l += 1
        return n-l


