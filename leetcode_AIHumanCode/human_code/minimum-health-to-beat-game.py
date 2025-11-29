# Time:  O(n)
# Space: O(1)

# greedy
class Solution(object):
    def minimumHealth(self, damage, armor):
        """
        """
        return sum(damage)-min(max(damage), armor)+1
