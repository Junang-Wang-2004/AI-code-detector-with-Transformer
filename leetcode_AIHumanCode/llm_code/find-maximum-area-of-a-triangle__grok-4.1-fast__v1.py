class Solution:
    def maxArea(self, coords):
        if not coords:
            return -1
        min_x = min_y = float('inf')
        max_x = max_y = float('-inf')
        ys_min_at_x = {}
        ys_max_at_x = {}
        xs_min_at_y = {}
        xs_max_at_y = {}
        for px, py in coords:
            min_x = min(min_x, px)
            max_x = max(max_x, px)
            min_y = min(min_y, py)
            max_y = max(max_y, py)
            if px not in ys_min_at_x:
                ys_min_at_x[px] = py
                ys_max_at_x[px] = py
            else:
                ys_min_at_x[px] = min(ys_min_at_x[px], py)
                ys_max_at_x[px] = max(ys_max_at_x[px], py)
            if py not in xs_min_at_y:
                xs_min_at_y[py] = px
                xs_max_at_y[py] = px
            else:
                xs_min_at_y[py] = min(xs_min_at_y[py], px)
                xs_max_at_y[py] = max(xs_max_at_y[py], px)
        ans = 0
        for cx in ys_min_at_x:
            ht = ys_max_at_x[cx] - ys_min_at_x[cx]
            wd = max(cx - min_x, max_x - cx)
            ans = max(ans, ht * wd)
        for cy in xs_min_at_y:
            wd = xs_max_at_y[cy] - xs_min_at_y[cy]
            ht = max(cy - min_y, max_y - cy)
            ans = max(ans, wd * ht)
        return ans if ans else -1
