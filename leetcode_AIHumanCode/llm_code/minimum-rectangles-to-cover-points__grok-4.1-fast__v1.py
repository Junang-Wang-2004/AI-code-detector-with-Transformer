class Solution:
    def minRectanglesToCoverPoints(self, points, w):
        xs = sorted(p[0] for p in points)
        n = len(xs)
        rects = 0
        i = 0
        while i < n:
            rects += 1
            start = xs[i]
            while i < n and xs[i] <= start + w:
                i += 1
        return rects
