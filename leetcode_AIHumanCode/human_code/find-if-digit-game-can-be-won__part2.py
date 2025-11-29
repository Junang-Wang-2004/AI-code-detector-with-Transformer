# Time:  O(n)
# Space: O(1)
# brute force, game theory
class Solution2(object):
    def canAliceWin(self, nums):
        """
        """
        return sum(x for x in nums if x < 10) != sum(x for x in nums if x >= 10)
