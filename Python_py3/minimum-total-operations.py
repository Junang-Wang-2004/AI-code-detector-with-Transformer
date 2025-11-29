# Time:  O(n)
# Space: O(1)

# array
class Solution(object):
    def minOperations(self, nums):
        """
        """
        return sum(nums[i] != nums[i+1] for i in range(len(nums)-1))
