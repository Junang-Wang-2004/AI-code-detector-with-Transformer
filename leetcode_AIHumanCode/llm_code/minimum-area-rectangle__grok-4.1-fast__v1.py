class Solution:
    def minAreaRect(self, points):
        point_set = {(x, y) for x, y in points}
        ans = float('inf')
        n = len(points)
        for i in range(n):
            a, b = points[i]
            for j in range(i + 1, n):
                c, d = points[j]
                if a != c and b != d:
                    if (a, d) in point_set and (c, b) in point_set:
                        area = abs(a - c) * abs(b - d)
                        ans = min(ans, area)
        return ans if ans < float('inf') else 0
