# Time:  O(1)
# Space: O(1)

# math
class Solution(object):
    def fillCups(self, amount):
        """
        """
        return max(max(amount), (sum(amount)+1)//2)


