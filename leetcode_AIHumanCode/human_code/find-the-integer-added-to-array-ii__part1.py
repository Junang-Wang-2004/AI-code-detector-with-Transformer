# Time:  O(n)
# Space: O(n)

import heapq
import collections


# partial sort, freq table
class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        """
        """
        def check(cnt2, cnt1):
            # return cnt2 <= cnt1  # for python3
            return all(cnt1.get(k, 0)-v >= 0 for k, v in cnt2.items())  # for python2
            
        mx = max(nums2)
        cnt2 = collections.Counter(nums2)
        return next(d for d in [mx-x for x in heapq.nlargest(3, nums1)] if check(cnt2, collections.Counter(x+d for x in nums1)))


