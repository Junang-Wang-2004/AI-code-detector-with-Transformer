# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        """
        count = [0]*2
        for p in chips:
            count[p%2] += 1
        return min(count)
