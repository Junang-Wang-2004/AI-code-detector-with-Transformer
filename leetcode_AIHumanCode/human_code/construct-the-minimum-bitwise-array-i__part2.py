# Time:  O(n * r)
# Space: O(1)
# brute force
class Solution2(object):
    def minBitwiseArray(self, nums):
        """
        """
        return [next((i for i in range(x) if i|(i+1) == x), -1) for x in nums]
