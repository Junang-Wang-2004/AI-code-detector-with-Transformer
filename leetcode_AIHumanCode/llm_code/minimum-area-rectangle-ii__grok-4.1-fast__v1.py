class Solution(object):
    def minAreaFreeRect(self, points):
        pt_set = set(tuple(p) for p in points)
        ans = float('inf')
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]
                dx1 = x2 - x1
                dy1 = y2 - y1
                for k in range(n):
                    if k == i or k == j:
                        continue
                    x3, y3 = points[k]
                    dx2 = x3 - x1
                    dy2 = y3 - y1
                    if dx1 * dx2 + dy1 * dy2 != 0:
                        continue
                    x4 = x1 + dx1 + dx2
                    y4 = y1 + dy1 + dy2
                    if (x4, y4) in pt_set:
                        area = (dx1 * dx1 + dy1 * dy1) * (dx2 * dx2 + dy2 * dy2)
                        ans = min(ans, area ** 0.5)
        return ans if ans < float('inf') else 0.0
