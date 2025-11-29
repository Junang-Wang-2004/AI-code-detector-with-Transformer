# Time:  O(nlogk)
# Space: O(k)

from sortedcontainers import SortedList


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        """
        sl = SortedList(float(nums[i])for i in range(k))
        result = [(sl[k//2]+sl[k//2-(1-k%2)])/2]
        for i in range(k, len(nums)):
            sl.add(float(nums[i]))
            sl.remove(nums[i-k])
            result.append((sl[k//2]+sl[k//2-(1-k%2)])/2)
        return result


