# Time:  O(n)
# Space: O(1)

# array
class Solution(object):
    def earliestTime(self, tasks):
        """
        """
        return min(s+t for s, t in tasks)
