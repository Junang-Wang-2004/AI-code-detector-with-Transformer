class Solution:
    def minimumDistance(self, points):
        n = len(points)
        if n < 2:
            return 0
        x, y = points[0]
        lo_s, hi_s = x + y, x + y
        lo_di, hi_di = x - y, x - y
        i_lo_s = i_hi_s = i_lo_di = i_hi_di = 0
        for i in range(1, n):
            x, y = points[i]
            val_s = x + y
            val_di = x - y
            if val_s < lo_s:
                lo_s = val_s
                i_lo_s = i
            if val_s > hi_s:
                hi_s = val_s
                i_hi_s = i
            if val_di < lo_di:
                lo_di = val_di
                i_lo_di = i
            if val_di > hi_di:
                hi_di = val_di
                i_hi_di = i
        span_s = hi_s - lo_s
        span_di = hi_di - lo_di
        if span_s >= span_di:
            skip_a = i_hi_s
            skip_b = i_lo_s
        else:
            skip_a = i_hi_di
            skip_b = i_lo_di

        def get_diam(skip):
            lo_s = hi_s = lo_di = hi_di = None
            for j in range(n):
                if j == skip:
                    continue
                x, y = points[j]
                vs = x + y
                vd = x - y
                if lo_s is None:
                    lo_s = hi_s = vs
                    lo_di = hi_di = vd
                else:
                    lo_s = min(lo_s, vs)
                    hi_s = max(hi_s, vs)
                    lo_di = min(lo_di, vd)
                    hi_di = max(hi_di, vd)
            return max(hi_s - lo_s, hi_di - lo_di)

        return min(get_diam(skip_a), get_diam(skip_b))
