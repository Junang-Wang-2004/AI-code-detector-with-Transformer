# Time:  O(n)
# Space: O(1)

# two pointers
class Solution(object):
    def countSubarrays(self, nums):
        """
        """
        result = l = 1
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                l = 0
            l += 1
            result += l
        return result


