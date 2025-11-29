# Time:  O(nlogn)
# Space: O(1)

# sort, greedy
class Solution(object):
    def maxCaloriesBurnt(self, heights):
        """
        """
        heights.sort()
        left, right = 0, len(heights)-1
        result = (0-heights[right])**2
        while left != right:
            result += (heights[right]-heights[left])**2
            right -= 1
            if left == right:
                break
            result += (heights[left]-heights[right])**2
            left += 1
        return result


