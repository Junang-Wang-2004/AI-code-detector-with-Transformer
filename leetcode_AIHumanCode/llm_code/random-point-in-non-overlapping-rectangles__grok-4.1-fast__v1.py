import random
import bisect

class Solution:

    def __init__(self, rectangles):
        self.bounds = [list(r) for r in rectangles]
        self.areas = [0]
        for x0, y0, x1, y1 in rectangles:
            sz = (x1 - x0 + 1) * (y1 - y0 + 1)
            self.areas.append(self.areas[-1] + sz)

    def pick(self):
        total = self.areas[-1]
        idx = random.randint(0, total - 1)
        rect_i = bisect.bisect_right(self.areas, idx) - 1
        offset = idx - self.areas[rect_i]
        r = self.bounds[rect_i]
        dx = offset % (r[2] - r[0] + 1)
        dy = offset // (r[2] - r[0] + 1)
        return [r[0] + dx, r[1] + dy]
