# Time:  O(n)
# Space: O(n)
import itertools


# sort
class Solution2(object):
    def canSortArray(self, nums):
        """
        """
        def popcount(x):
            return bin(x).count("1")
        
        def pairwise(it):
            a, b = tee(it)
            next(b, None)
            return zip(a, b)

        return all(max(a) <= min(b) for a, b in pairwise(list(it) for key, it in groupby(nums, popcount)))


