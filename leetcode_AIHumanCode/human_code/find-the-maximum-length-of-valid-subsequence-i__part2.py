# Time:  O(n)
# Space: O(1)
# brute force
class Solution2(object):
    def maximumLength(self, nums):
        """
        """
        return max(sum(x%2 == 0 for x in nums),
                   sum(x%2 == 1 for x in nums),
                   sum(nums[i]%2 != nums[i+1]%2 for i in range(len(nums)-1))+1)
