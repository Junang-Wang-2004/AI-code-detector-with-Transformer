import collections
import math

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Solution(object):
    def maxPoints(self, points):
        n = len(points)
        best = 0
        for i in range(n):
            repeats = 1
            lines = collections.defaultdict(int)
            for j in range(i + 1, n):
                dx = points[i].x - points[j].x
                dy = points[i].y - points[j].y
                if dx == 0 and dy == 0:
                    repeats += 1
                else:
                    g = math.gcd(abs(dx), abs(dy))
                    dx //= g
                    dy //= g
                    if dx < 0 or (dx == 0 and dy < 0):
                        dx = -dx
                        dy = -dy
                    lines[(dy, dx)] += 1
            curr = repeats
            for cnt in lines.values():
                curr = max(curr, cnt + repeats)
            best = max(best, curr)
        return best
