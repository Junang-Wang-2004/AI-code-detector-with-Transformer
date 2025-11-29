# Time:  O(n)
# Space: O(n)
class Solution4(object):
    def trap(self, height):
        """
        """
        result = 0
        stk = []
        for i in range(len(height)):
            prev = 0
            while stk and height[stk[-1]] <= height[i]:
                j = stk.pop()
                result += (height[j] - prev) * (i - j - 1)
                prev = height[j]
            if stk:
                result += (height[i] - prev) * (i - stk[-1] - 1)
            stk.append(i)
        return result
