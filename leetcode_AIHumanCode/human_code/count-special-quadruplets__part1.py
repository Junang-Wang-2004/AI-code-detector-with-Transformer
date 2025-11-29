# Time:  O(n^3)
# Space: O(n)

import collections


class Solution(object):
    def countQuadruplets(self, nums):
        """
        """
        result = 0
        lookup = collections.defaultdict(int)
        lookup[nums[-1]] = 1
        for c in reversed(range(2, len(nums)-1)):
            for b in range(1, c):
                for a in range(b):
                    if nums[a]+nums[b]+nums[c] in lookup:
                        result += lookup[nums[a]+nums[b]+nums[c]]
            lookup[nums[c]] += 1
        return result

    
