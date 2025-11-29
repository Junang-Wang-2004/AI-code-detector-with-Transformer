# Time:  O(n)
# Space: O(1)

# bit manipulation
class Solution(object):
    def subsequenceSumOr(self, nums):
        """
        """
        result = prefix = 0
        for x in nums:
            prefix += x
            result |= x|prefix
        return result


