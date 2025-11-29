# Time:  O(n)
# Space: O(n)

import collections


class Solution(object):
    def subarraysWithMoreZerosThanOnes(self, nums):
        """
        """
        MOD = 10**9+7

        lookup = collections.defaultdict(int)
        lookup[0] = 1
        result = total = same = more = 0
        for x in nums:
            total += 1 if x == 1 else -1
            new_same = lookup[total]
            new_more = (same+more+1)%MOD if x == 1 else (more-new_same)%MOD
            lookup[total] += 1
            result = (result+new_more)%MOD
            same, more = new_same, new_more
        return result


