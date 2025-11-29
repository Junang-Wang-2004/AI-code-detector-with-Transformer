# Time:  O(n)
# Space: O(n)
# prefix sum, CodeChef Starters 146 - Bouncing Ball (https://www.codechef.com/problems/BOUNCE_BALL)
class Solution2(object):
    def countValidSelections(self, nums):
        """
        """
        prefix = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        suffix = [0]*(len(nums)+1)
        for i in reversed(range(len(nums))):
            suffix[i] = suffix[i+1]+nums[i]
        return sum(max(2-abs(prefix[i]-suffix[i+1]), 0) for i in range(len(nums)) if nums[i] == 0)
