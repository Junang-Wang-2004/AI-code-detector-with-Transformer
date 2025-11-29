class Solution:
    def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
        left = x1 - x_center
        right = x2 - x_center
        bottom = y1 - y_center
        top = y2 - y_center
        cx = max(left, min(0, right))
        cy = max(bottom, min(0, top))
        return cx * cx + cy * cy <= radius * radius
