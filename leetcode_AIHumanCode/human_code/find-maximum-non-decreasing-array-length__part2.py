# Time:  O(n)
# Space: O(n)
import collections


# greedy, prefix sum, mono deque
class Solution2(object):
    def findMaximumLength(self, nums):
        """
        """
        dp = prefix = prev_prefix = prev_dp = 0
        dq = collections.deque()
        for right in range(len(nums)):
            prefix += nums[right]
            while dq and dq[0][0] <= prefix:
                _, prev_prefix, prev_dp = dq.popleft()
            last, dp = prefix-prev_prefix, prev_dp+1
            while dq and dq[-1][0] >= last+prefix:
                dq.pop()
            dq.append((last+prefix, prefix, dp))
        return dp


