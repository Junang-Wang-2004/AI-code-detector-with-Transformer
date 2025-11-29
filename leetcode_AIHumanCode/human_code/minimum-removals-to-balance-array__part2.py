# Time:  O(nlogn)
# Space: O(1)
# sort, two pointers
class Solution2(object):
    def minRemoval(self, nums, k):
        """
        """
        nums.sort()
        result = left = 0
        for right in range(len(nums)):
            while nums[left]*k < nums[right]:
                left += 1
            result = max(result, right-left+1)
        return len(nums)-result
