# Time:  O(n)
# Space: O(1)

class Solution(object):
    def trap(self, height):
        """
        """
        result, left, right, level = 0, 0, len(height)-1, 0
        while left < right:
            if height[left] < height[right]:
                lower = height[left]
                left += 1
            else:
                lower = height[right]
                right -= 1
            level = max(level, lower)
            result += level-lower
        return result


