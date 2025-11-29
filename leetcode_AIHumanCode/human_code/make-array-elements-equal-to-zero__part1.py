# Time:  O(n)
# Space: O(1)

# prefix sum, CodeChef Starters 146 - Bouncing Ball (https://www.codechef.com/problems/BOUNCE_BALL)
class Solution(object):
    def countValidSelections(self, nums):
        """
        """
        total = sum(nums)
        result = curr = 0
        for x in nums:
            if not x:
                result += max(2-abs(curr-(total-curr)), 0)
            else:
                curr += x
        return result


