# Time:  O(n! * nlogr)
# Space: O(nlogr)
import itertools


# brute force
class Solution2(object):
    def maxGoodNumber(self, nums):
        """
        """
        return max(int("".join(x), 2) for x in itertools.permutations([bin(x)[2:] for x in nums]))
