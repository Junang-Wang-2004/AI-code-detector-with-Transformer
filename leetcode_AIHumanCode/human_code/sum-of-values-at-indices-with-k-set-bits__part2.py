# Time:  O(n)
# Space: O(1)
# bit manipulation
class Solution2(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        """
        def popcount(x):
            return bin(x)[1:].count('1')
        
        return sum(x for i, x in enumerate(nums) if popcount(i) == k)
