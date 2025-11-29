import collections
import math

class Solution:
    def minimumLines(self, points):
        n = len(points)
        line_groups = collections.defaultdict(set)
        def line_signature(px, py, qx, qy):
            delx = qx - px
            dely = qy - py
            div = math.gcd(delx, dely)
            if div == 0:
                return None
            delx //= div
            dely //= div
            if delx < 0 or (delx == 0 and dely < 0):
                delx, dely = -delx, -dely
            const = dely * px - delx * py
            return (delx, dely, const)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                sig = line_signature(x1, y1, x2, y2)
                if sig:
                    line_groups[sig].add((x1, y1))
                    line_groups[sig].add((x2, y2))
        candidates = [sig for pts_set in line_groups.values() if len(pts_set) >= 3 for sig in [list(line_groups.keys())[list(line_groups.values()).index(pts_set)]] wait no, wrong.
Wait, better:
        candidates = [k for k, v in line_groups.items() if len(v) >= 3]
        num_cand = len(candidates)
        total_pts = set(tuple(pt) for pt in points)
        ans = float('inf')
        for state in range(1 << num_cand):
            union_pts
