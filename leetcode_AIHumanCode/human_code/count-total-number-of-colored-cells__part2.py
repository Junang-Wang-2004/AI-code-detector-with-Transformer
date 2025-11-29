# Time:  O(1)
# Space: O(1)
# math
class Solution2(object):
    def coloredCells(self, n):
        """
        """
        return (1+(1+2*(n-1)))*n//2*2-(2*n-1)
