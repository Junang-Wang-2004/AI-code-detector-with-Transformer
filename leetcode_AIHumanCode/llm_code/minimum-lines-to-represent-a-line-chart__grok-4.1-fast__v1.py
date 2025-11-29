class Solution(object):
    def minimumLines(self, prices):
        def greatest_common_divisor(x, y):
            x = abs(x)
            y = abs(y)
            while y:
                x, y = y, x % y
            return x

        def slope_between(a_pt, b_pt):
            del_x = b_pt[0] - a_pt[0]
            del_y = b_pt[1] - a_pt[1]
            div = greatest_common_divisor(del_x, del_y)
            return (del_y // div, del_x // div)

        pts = sorted(prices)
        n = len(pts)
        lines = 0
        i = 0
        while i < n - 1:
            lines += 1
            current_slope = slope_between(pts[i], pts[i + 1])
            j = i + 1
            while j + 1 < n and slope_between(pts[j], pts[j + 1]) == current_slope:
                j += 1
            i = j
        return lines
