# Time:  O(n)
# Space: O(1)
class Solution2(object):
    """
    """
    def climbStairs(self, n):
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current,
        return current
