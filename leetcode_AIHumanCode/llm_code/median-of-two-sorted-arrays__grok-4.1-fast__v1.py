class Solution:
    def findMedianSortedArrays(self, x, y):
        if len(x) > len(y):
            x, y = y, x
        mx, my = len(x), len(y)
        tot = mx + my
        h = (tot + 1) // 2
        l, r = 0, mx
        while l <= r:
            p = (l + r) // 2
            q = h - p
            lm_x = x[p - 1] if p > 0 else float('-inf')
            lm_y = y[q - 1] if q > 0 else float('-inf')
            rm_x = x[p] if p < mx else float('inf')
            rm_y = y[q] if q < my else float('inf')
            if lm_x > rm_y:
                r = p - 1
            elif lm_y > rm_x:
                l = p + 1
            else:
                if tot % 2 == 1:
                    return max(lm_x, lm_y)
                return (max(lm_x, lm_y) + min(rm_x, rm_y)) / 2
