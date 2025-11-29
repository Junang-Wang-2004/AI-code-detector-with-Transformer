# Time:  O(nlogk)
# Space: O(k)

import collections
from sortedcontainers import SortedList


# sorted list, two pointers, sliding window
class Solution(object):
    def modeWeight(self, nums, k):
        """
        """
        def add(x, diff):
            if cnt[x]:
                sl.remove((-cnt[x], x))
            cnt[x] += diff
            if cnt[x]:
                sl.add((-cnt[x], x))
            else:
                del cnt[x]
    
        cnt = collections.defaultdict(int)
        sl = SortedList()
        result = 0
        for i in range(len(nums)):
            add(nums[i], +1)
            if i >= k-1:
                result += -sl[0][0]*sl[0][1]
                add(nums[i-k+1], -1)
        return result


