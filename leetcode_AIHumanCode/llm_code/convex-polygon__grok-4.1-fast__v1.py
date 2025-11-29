class Solution:
    def isConvex(self, points):
        n = len(points)
        direction = 0
        for i in range(n):
            x0, y0 = points[i]
            x1, y1 = points[(i + 1) % n]
            x2, y2 = points[(i + 2) % n]
            cr = (x1 - x0) * (y2 - y1) - (y1 - y0) * (x2 - x1)
            if cr != 0:
                sgn = 1 if cr > 0 else -1
                if direction and direction != sgn:
                    return False
                direction = sgn
        return True
