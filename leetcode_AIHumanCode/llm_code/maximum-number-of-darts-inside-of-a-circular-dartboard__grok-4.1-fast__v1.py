import math

class Solution(object):
    def numPoints(self, points, r):
        n = len(points)
        ans = 0
        for i in range(n):
            duplicates = 1
            events = []
            for j in range(n):
                if i == j:
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dist_sq = dx * dx + dy * dy
                if dist_sq == 0:
                    duplicates += 1
                    continue
                if dist_sq > 4 * r * r:
                    continue
                dist = math.sqrt(dist_sq)
                direction = math.atan2(dy, dx)
                spread = math.acos(dist / (2 * r))
                events.append((direction - spread, False))
                events.append((direction + spread, True))
            events.sort(key=lambda e: (e[0], e[1]))
            current = duplicates
            local_max = duplicates
            for _, is_end in events:
                if is_end:
                    current -= 1
                else:
                    current += 1
                local_max = max(local_max, current)
            ans = max(ans, local_max)
        return ans
