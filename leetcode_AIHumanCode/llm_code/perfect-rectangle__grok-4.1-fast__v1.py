from collections import Counter

class Solution(object):
    def isRectangleCover(self, rectangles):
        if not rectangles:
            return False
        min_x = min(r[0] for r in rectangles)
        max_x = max(r[2] for r in rectangles)
        min_y = min(r[1] for r in rectangles)
        max_y = max(r[3] for r in rectangles)
        total_area = sum((r[2] - r[0]) * (r[3] - r[1]) for r in rectangles)
        bbox_area = (max_x - min_x) * (max_y - min_y)
        if total_area != bbox_area:
            return False
        count = Counter()
        for x1, y1, x2, y2 in rectangles:
            count[(x1, y1)] += 1
            count[(x2, y1)] += 1
            count[(x1, y2)] += 1
            count[(x2, y2)] += 1
        extremes = {
            (min_x, min_y),
            (max_x, min_y),
            (min_x, max_y),
            (max_x, max_y)
        }
        for corner in extremes:
            if count[corner] != 1:
                return False
        for pos, freq in count.items():
            if pos not in extremes:
                if freq % 2 != 0:
                    return False
        return True
