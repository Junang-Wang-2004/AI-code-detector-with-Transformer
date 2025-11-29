# Time:  O(n)
# Space: O(n)
import collections


# freq table
class Solution2(object):
    def specialTriplets(self, nums):
        """
        """
        MOD = 10**9+7
        result = 0
        right = collections.defaultdict(int)
        for x in nums:
            right[x] += 1
        left = collections.defaultdict(int)
        for x in nums:
            right[x] -= 1
            if not right[x]:
                del right[x]
            if 2*x in left and 2*x in right:
                result = (result+left[2*x]*right[2*x])%MOD
            left[x] += 1
        return result
