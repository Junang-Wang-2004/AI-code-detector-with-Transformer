# Time:  O(nlogn)
# Space: O(n)
import collections


class Solution3(object):
    def majorityElement(self, nums):
        """
        """
        return sorted(list(collections.Counter(nums).items()), key=lambda a: a[1], reverse=True)[0][0]
