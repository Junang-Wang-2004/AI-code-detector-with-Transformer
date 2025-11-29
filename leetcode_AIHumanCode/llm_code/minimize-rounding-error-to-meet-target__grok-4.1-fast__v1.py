import math

class Solution:
    def minimizeError(self, prices, target):
        total_floor = 0
        fractions = []
        num_frac = 0
        for price_str in prices:
            val = float(price_str)
            floored = int(val)
            total_floor += floored
            frac_part = val - floored
            if frac_part > 0:
                fractions.append(frac_part)
                num_frac += 1
        total_ceil = total_floor + num_frac
        if total_floor > target or total_ceil < target:
            return "-1"
        needed_ceil = target - total_floor
        needed_floor = num_frac - needed_ceil
        fractions.sort()
        error_sum = sum(fractions[:needed_floor])
        for i in range(needed_floor, num_frac):
            error_sum += 1 - fractions[i]
        return f"{error_sum:.3f}"
