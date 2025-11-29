# Time:  O(n)
# Space: O(1)

# brute force, game theory
class Solution(object):
    def canAliceWin(self, nums):
        """
        """
        total1 = total2 = 0
        for x in nums:
            if x < 10:
                total1 += x
            else:
                total2 += x
        return total1 != total2


