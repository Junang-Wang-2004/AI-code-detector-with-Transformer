# Time:  O(n)
# Space: O(n)

# dp, greedy, prefix sum, mono stack, two pointers
class Solution(object):
    def findMaximumLength(self, nums):
        """
        """
        dp = prefix = left = 0
        stk = [(0, 0, 0)]
        for right in range(len(nums)):
            prefix += nums[right]
            while left+1 < len(stk) and stk[left+1][0] <= prefix:
                left += 1
            last, dp = prefix-stk[left][1], stk[left][2]+1
            while stk and stk[-1][0] >= last+prefix:
                stk.pop()
            stk.append((last+prefix, prefix, dp))
            left = min(left, len(stk)-1)
        return dp


