# Time:  O(nlogn)
# Space: O(n)
from sortedcontainers import SortedList


# sorted list
class Solution2(object):
    def kBigIndices(self, nums, k):
        """
        """
        sl1, sl2 = SortedList(), SortedList(nums)
        result = 0
        for x in nums:
            sl2.remove(x)
            if sl1.bisect_left(x) >= k and sl2.bisect_left(x) >= k:
                result += 1
            sl1.add(x)
        return result
