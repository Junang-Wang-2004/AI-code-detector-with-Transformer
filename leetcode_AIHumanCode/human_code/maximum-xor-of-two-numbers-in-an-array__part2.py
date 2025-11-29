# Time:  O(nlogr), r = max(nums)
# Space: O(n)
class Solution2(object):
    def findMaximumXOR(self, nums):
        """
        """
        result = 0
        for i in reversed(range(max(nums).bit_length())):
            result <<= 1
            prefixes = set()
            for n in nums:
                prefixes.add(n >> i)
            for p in prefixes:
                if (result | 1) ^ p in prefixes:
                    result |= 1
                    break
        return result
