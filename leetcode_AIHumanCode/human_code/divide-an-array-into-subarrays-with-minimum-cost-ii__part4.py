# Time:  O(nlogd)
# Space: O(d)
from sortedcontainers import SortedList


# sliding window, sorted list
class Solution4(object):
    def minimumCost(self, nums, k, dist):
        """
        """
        sl = SortedList(nums[1:1+(1+dist)])
        mn = curr = sum(sl[:k-1])
        for i in range(1+(1+dist), len(nums)):
            sl.add(nums[i])
            curr += min(nums[i]-sl[k-1], 0)
            curr -= min(nums[i-(1+dist)]-sl[k-1], 0)
            sl.remove(nums[i-(1+dist)])
            mn = min(mn, curr)
        return nums[0]+mn
