# Time:  O(n * l)
# Space: O(1)

# string
class Solution(object):
    def maximumValue(self, strs):
        """
        """
        return max(int(s) if s.isdigit() else len(s) for s in strs)
