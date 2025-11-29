# Time:  O(n)
# Space: O(n)
import collections


class Solution2(object):
    def majorityElement(self, nums):
        """
        """
        return collections.Counter(nums).most_common(1)[0][0]


