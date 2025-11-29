import math

class Solution:
    def visiblePoints(self, points, angle, location):
        directions = []
        duplicates = 0
        lx, ly = location
        for px, py in points:
            if px == lx and py == ly:
                duplicates += 1
                continue
            dx = px - lx
            dy = py - ly
            directions.append(math.atan2(dy, dx))
        directions.sort()
        doubled = directions + [theta + 2 * math.pi for theta in directions]
        cone = math.radians(angle)
        maximum = 0
        begin = 0
        for finish in range(len(doubled)):
            while doubled[finish] - doubled[begin] > cone:
                begin += 1
            maximum = max(maximum, finish - begin + 1)
        return maximum + duplicates
