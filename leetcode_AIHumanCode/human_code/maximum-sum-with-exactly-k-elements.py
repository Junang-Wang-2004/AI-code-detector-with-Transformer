# Time:  O(n)
# Space: O(1)

# math
class Solution(object):
    def maximizeSum(self, nums, k):
        """
        """
        return max(nums)*k+k*(k-1)//2
