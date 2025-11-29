# Time:  O(n)
# Space: O(n)
class Solution3(object):
    def trap(self, height):
        """
        """
        right = [0]*len(height)
        mx = 0
        for i in reversed(range(len(height))):
            right[i] = mx
            mx = max(mx, height[i])
        result = left = 0
        for i in range(len(height)):
            left = max(left, height[i])
            result += max(min(left, right[i])-height[i], 0)
        return result


