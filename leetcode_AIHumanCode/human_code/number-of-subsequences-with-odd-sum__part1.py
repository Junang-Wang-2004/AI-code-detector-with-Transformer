# Time:  O(n)
# Space: O(1)

# combinatorics, fast exponentiation
class Solution(object):
    def subsequenceCount(self, nums):
        """
        """
        MOD = 10**9+7
        # 2^(odd-1)*2^even = 2^(len(nums)-1)
        return pow(2, len(nums)-1, MOD) if any(x%2 for x in nums) else 0


