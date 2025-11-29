import random

class Solution(object):
    def outerTrees(self, trees):
        def point_dist_sq(x1, y1, x2, y2):
            dx = x1 - x2
            dy = y1 - y2
            return dx * dx + dy * dy

        def point_in_circle(cx, cy, cr, px, py):
            return point_dist_sq(cx, cy, px, py) <= cr * cr + 1e-9

        def make_circle_two(p, q):
            cx = (p[0] + q[0]) / 2
            cy = (p[1] + q[1]) / 2
            dr = ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5 / 2
            return cx, cy, dr

        def make_circle_three(a, b, c):
            ax, ay = a
            bx, by = b
            cx, cy = c
            denom_part = ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)
            denom = 2 * denom_part
            if abs(denom) < 1e-9:
                da_b = point_dist_sq(ax, ay, bx, by)
                da_c = point_dist_sq(ax, ay, cx, cy)
                db_c = point_dist_sq(bx, by, cx, cy)
                if da_b >= da_c and da_b >= db_c:
                    return make_circle_two(a, b)
                if da_c >= da_b and da_c >= db_c:
                    return make_circle_two(a, c)
                return make_circle_two(b, c)
            a2 = ax * ax + ay * ay
            b2 = bx * bx + by * by
            c2 = cx * cx + cy * cy
            hx = (a2 * (by - cy) + b2 * (cy - ay) + c2 * (ay - by)) / denom
            hy = (a2 * (cx - bx) + b2 * (ax - cx) + c2 * (bx - ax)) / denom
            dr = ((hx - ax) ** 2 + (hy - ay) ** 2) ** 0.5
            return hx, hy, dr

        def trivial_case(on_hull):
            sz = len(on_hull)
            if sz == 0:
                return 0.0, 0.0, 0.0
            if sz == 1:
                return on_hull[0][0], on_hull[0][1], 0.0
            if sz == 2:
                return make_circle_two(on_hull[0], on_hull[1])
            return make_circle_three(on_hull[0], on_hull[1], on_hull[2])

        def find_min_circle(all_pts, hull_pts, pos):
            if pos == len(all_pts) or len(hull_pts) == 3:
                return trivial_case(hull_pts)
            without_p = find_min_circle(all_pts, hull_pts, pos + 1)
            px, py = all_pts[pos]
            if point_in_circle(*without_p, px, py):
                return without_p
            hull_pts.append(all_pts[pos])
            with_p = find_min_circle(all_pts, hull_pts, pos + 1)
            hull_pts.pop()
            return with_p

        pts_copy = trees[:]
        random.shuffle(pts_copy)
        min_circ = find_min_circle(pts_copy, [], 0)
        return min_circ
