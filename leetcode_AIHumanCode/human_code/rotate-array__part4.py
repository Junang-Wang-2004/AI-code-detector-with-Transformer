# Time:  O(n)
# Space: O(n)
class Solution4(object):
    """
    """
    def rotate(self, nums, k):
        """
        """
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
        

