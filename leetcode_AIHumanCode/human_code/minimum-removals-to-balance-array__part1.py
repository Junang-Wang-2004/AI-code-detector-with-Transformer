# Time:  O(nlogn)
# Space: O(1)

# sort, two pointers
class Solution(object):
    def minRemoval(self, nums, k):
        """
        """
        nums.sort()
        left = 0
        for right in range(len(nums)):
            if nums[left]*k < nums[right]:
                left += 1
        return left


