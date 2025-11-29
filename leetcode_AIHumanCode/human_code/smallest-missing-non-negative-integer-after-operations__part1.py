# Time:  O(n)
# Space: O(k), k = value

import collections


# freq table
class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        """
        cnt = collections.Counter(x%value for x in nums)
        mn = min((cnt[i], i) for i in range(value))[1]
        return value*cnt[mn]+mn
        

