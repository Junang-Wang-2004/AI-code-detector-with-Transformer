# Time:  O(k * n) = O(n^2), k is len(nums)
#                         , n is len(nums[0])
# Space: O(k) = O(n)
class Solution2(object):
    def findDifferentBinaryString(self, nums):
        """
        """
        lookup = set([int(x, 2) for x in nums])  # Time: O(k * n) = O(n^2)
        return next(bin(i)[2:].zfill(len(nums[0])) for i in range(2**len(nums[0])) if i not in lookup)  # Time: O(k + n) = O(n)


