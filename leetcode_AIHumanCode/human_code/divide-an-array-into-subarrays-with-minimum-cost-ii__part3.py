# Time:  O(nlogd)
# Space: O(d)
from sortedcontainers import SortedList


# sliding window, sorted list
class Solution3(object):
    def minimumCost(self, nums, k, dist):
        """
        """
        sl1, sl2 = SortedList(), SortedList()
        mn, curr = float("inf"), 0
        for i in range(1, len(nums)):
            sl1.add(nums[i])
            curr += nums[i]
            if len(sl1) > k-1:
                curr -= sl1[-1]
                sl2.add(sl1.pop())
            if len(sl1)+len(sl2) > 1+dist:
                if sl2[0] <= nums[i-(1+dist)]:
                    sl2.remove(nums[i-(1+dist)])
                else:
                    sl1.remove(nums[i-(1+dist)])
                    curr -= nums[i-(1+dist)]-sl2[0]
                    sl1.add(sl2.pop(0))
            if len(sl1) == k-1:
                mn = min(mn, curr)
        return nums[0]+mn


