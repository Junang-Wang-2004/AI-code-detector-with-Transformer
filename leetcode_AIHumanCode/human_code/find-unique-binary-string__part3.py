# Time:  O(k * n + n * 2^n) = O(n * 2^n), k is len(nums)
#                                       , n is len(nums[0])
# Space: O(k) = O(1) ~ O(2^n)
class Solution_Extra(object):
    def findAllDifferentBinaryStrings(self, nums):
        """
        """
        lookup = set([int(x, 2) for x in nums])  # Time: O(k * n) = O(n * 2^n)
        return [bin(i)[2:].zfill(len(nums[0])) for i in range(2**len(nums[0])) if i not in lookup]  # Time: O(2^n + n * (2^n - k))
