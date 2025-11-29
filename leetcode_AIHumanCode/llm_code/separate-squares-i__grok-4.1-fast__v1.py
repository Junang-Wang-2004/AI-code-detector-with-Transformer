class Solution:
    def separateSquares(self, squares):
        if not squares:
            return 0.0
        min_height = min(y for _, y, _ in squares)
        max_height = max(y + l for _, y, l in squares)
        full_area = sum(l * l for _, _, l in squares)
        target = full_area / 2.0

        def area_under(height):
            accum = 0.0
            for _, bottom, side in squares:
                if height > bottom:
                    if height >= bottom + side:
                        accum += side * side
                    else:
                        accum += side * (height - bottom)
            return accum

        lo, hi = min_height, max_height
        while hi - lo > 1e-10:
            mid = (lo + hi) / 2
            if area_under(mid) >= target:
                hi = mid
            else:
                lo = mid
        return lo
