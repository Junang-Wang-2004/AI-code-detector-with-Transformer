class Solution:
    def countLatticePoints(self, circles):
        min_x = min(cx - rad for cx, _, rad in circles)
        max_x = max(cx + rad for cx, _, rad in circles)
        min_y = min(cy - rad for _, cy, rad in circles)
        max_y = max(cy + rad for _, cy, rad in circles)
        covered = set()
        for px in range(min_x, max_x + 1):
            for py in range(min_y, max_y + 1):
                for cx, cy, rad in circles:
                    if (px - cx) ** 2 + (py - cy) ** 2 <= rad ** 2:
                        covered.add((px, py))
                        break
        return len(covered)
