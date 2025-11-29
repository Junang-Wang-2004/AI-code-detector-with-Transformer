class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 0
        prev = float('-inf')
        for start, end in points:
            if start > prev:
                arrows += 1
                prev = end
        return arrows
