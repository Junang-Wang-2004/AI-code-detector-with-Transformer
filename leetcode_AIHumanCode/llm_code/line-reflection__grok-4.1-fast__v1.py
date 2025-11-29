class Solution:
    def isReflected(self, points):
        if not points:
            return True
        point_set = set(tuple(pt) for pt in points)
        min_x = min(pt[0] for pt in points)
        max_x = max(pt[0] for pt in points)
        reflect_base = min_x + max_x
        for pt in points:
            x, y = pt
            mirror_x = reflect_base - x
            if (mirror_x, y) not in point_set:
                return False
        return True
