# Time:  O(1)
# Space: O(1)

class Solution(object):
    def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
        """
        """
        x1 -= x_center
        y1 -= y_center
        x2 -= x_center
        y2 -= y_center
        x = x1 if x1 > 0 else x2 if x2 < 0 else 0
        y = y1 if y1 > 0 else y2 if y2 < 0 else 0
        return x**2 + y**2 <= radius**2


