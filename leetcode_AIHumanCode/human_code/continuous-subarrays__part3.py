# Time:  O(nlogn)
# Space: O(n)
from sortedcontainers import SortedDict


# ordered dict, two pointers
class Solution3(object):
    def continuousSubarrays(self, nums):
        """
        """
        result = left = 0
        lookup = SortedDict()
        for right in range(len(nums)):
            lookup[nums[right]] = right
            to_del = []
            for x, i in list(lookup.items()):
                if nums[right]-x <= 2:
                    break
                left = max(left, i+1)
                to_del.append(x)
            for x, i in reversed(list(lookup.items())):
                if x-nums[right] <= 2:
                    break
                left = max(left, i+1)
                to_del.append(x) 
            for x in to_del:
                del lookup[x]
            result += right-left+1
        return result
