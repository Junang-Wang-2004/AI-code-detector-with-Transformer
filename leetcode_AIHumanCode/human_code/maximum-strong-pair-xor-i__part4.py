# Time:  O(n^2)
# Space: O(1)
# bit manipulation, brute force
class Solution4(object):
    def maximumStrongPairXor(self, nums):
        """
        """
        return max(nums[i]^nums[j] for i in range(len(nums)) for j in range(i, len(nums)) if abs(nums[i]-nums[j]) <= min(nums[i], nums[j]))
