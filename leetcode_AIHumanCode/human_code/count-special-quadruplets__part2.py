# Time:  O(n^2) ~ O(n^4)
# Space: O(n^2)
import collections


class Solution2(object):
    def countQuadruplets(self, nums):
        """
        """
        lookup = collections.defaultdict(list)
        for d in range(3, len(nums)):
            for c in range(2, d):
                lookup[nums[d]-nums[c]].append(c)
        return sum(sum(b < c for c in lookup[nums[a]+nums[b]]) for b in range(1, len(nums)-2) for a in range(b))
