class Solution:
    def largestTriangleArea(self, points):
        max_area = 0.0
        n = len(points)
        for a in range(n):
            xa, ya = points[a]
            for b in range(a + 1, n):
                xb, yb = points[b]
                for c in range(b + 1, n):
                    xc, yc = points[c]
                    area = 0.5 * abs((xb - xa) * (yc - ya) - (xc - xa) * (yb - ya))
                    if area > max_area:
                        max_area = area
        return max_area
