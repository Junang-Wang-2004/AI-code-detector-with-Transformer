# Time:  O(n)
# Space: O(n)

class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        """
        result = [0]*len(heights)
        stk = []
        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] < h:
                result[stk.pop()] += 1
            if stk:
                result[stk[-1]] += 1
            if stk and heights[stk[-1]] == h:
                stk.pop()
            stk.append(i)
        return result


