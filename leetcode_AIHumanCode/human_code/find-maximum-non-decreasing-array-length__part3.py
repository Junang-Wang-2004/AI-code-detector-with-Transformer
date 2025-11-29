# Time:  O(nlogn)
# Space: O(n)
import bisect


# dp, greedy, prefix sum, mono stack, binary search
class Solution3(object):
    def findMaximumLength(self, nums):
        """
        """
        dp = prefix = left = 0
        stk = [(0, 0, 0)]
        for right in range(len(nums)):
            prefix += nums[right]
            left = bisect.bisect_left(stk, (prefix+1, 0, 0))-1
            last, dp = prefix-stk[left][1], stk[left][2]+1
            while stk and stk[-1][0] >= last+prefix:
                stk.pop()
            stk.append((last+prefix, prefix, dp))
        return dp


