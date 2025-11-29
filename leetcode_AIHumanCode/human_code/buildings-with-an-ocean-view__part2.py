# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def findBuildings(self, heights):
        """
        """
        result = []
        for i in reversed(range(len(heights))):
            if not result or heights[result[-1]] < heights[i]:
                result.append(i)
        result.reverse()
        return result
