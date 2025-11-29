# Time:  O(n)
# Space: O(n)

class Solution(object):
    def findBuildings(self, heights):
        """
        """
        result = []
        for i, h in enumerate(heights):
            while result and heights[result[-1]] <= h:
                result.pop()
            result.append(i)
        return result


