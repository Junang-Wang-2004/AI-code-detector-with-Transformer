# Time:  O(n)
# Space: O(1)

class Solution(object):
    def addRungs(self, rungs, dist):
        """
        """
        def ceil_divide(a, b):
            return (a+(b-1))//b

        result = prev = 0
        for curr in rungs:
            result += ceil_divide(curr-prev, dist)-1
            prev = curr
        return result
