# Time:  O(sqrt(n))
# Space: O(1)
# simulation
class Solution2(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        """
        def f(x, y):
            h = 0
            while x >= h+1:
                h += 1
                x -= h
                x, y = y, x
            return h

        return max(f(red, blue), f(blue, red))
