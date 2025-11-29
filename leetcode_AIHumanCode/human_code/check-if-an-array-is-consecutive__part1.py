# Time:  O(n)
# Space: O(n)

# hash table
class Solution(object):
    def isConsecutive(self, nums):
        """
        """
        return max(nums)-min(nums)+1 == len(nums) == len(set(nums))


