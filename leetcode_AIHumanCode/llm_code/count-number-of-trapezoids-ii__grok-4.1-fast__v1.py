import collections

class Solution:
    def countTrapezoids(self, pts):
        def reduce_frac(dx, dy):
            g = 0
            adx, ady = abs(dx), abs(dy)
            while ady:
                adx, ady = ady, adx % ady
            g = adx
            if g == 0:
                return 0, 0
            sx = dx // g
            sy = dy // g
            if sx < 0 or (sx == 0 and sy < 0):
                sx, sy = -sx, -sy
            return sx, sy

        slope_freq = collections.defaultdict(int)
        line_freq = collections.defaultdict(int)
        slope_len_freq = collections.defaultdict(int)
        line_len_freq = collections.defaultdict(int)
        traps = 0
        eq_len = 0
        n = len(pts)
        for i in range(n):
            xi, yi = pts[i]
            for j in range(i):
                xj, yj = pts[j]
                dx = xj - xi
                dy = yj - yi
                sx, sy = reduce_frac(dx, dy)
                if sx == 0 and sy == 0:
                    continue
                const = sy * xi - sx * yi
                line_id = (sx, sy, const)
                dist2 = dx * dx + dy * dy
                len_slope_id = (sx, sy, dist2)
                len_line_id = (sx, sy, const, dist2)
                traps += slope_freq[(sx, sy)] - line_freq[line_id]
                eq_len += slope_len_freq[len_slope_id] - line_len_freq[len_line_id]
                slope_freq[(sx, sy)] += 1
                line_freq[line_id] += 1
                slope_len_freq[len_slope_id] += 1
                line_len_freq[len_line_id] += 1
        return traps - (eq_len // 2)
