class Solution:
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        min_time = min(workerTimes)
        left = min_time * mountainHeight
        right = min_time * mountainHeight * (mountainHeight + 1) // 2

        def feasible(seconds):
            total_layers = 0
            for t in workerTimes:
                lo, hi = 0, mountainHeight
                while lo < hi:
                    mid = (lo + hi + 1) // 2
                    if t * (mid * (mid + 1) // 2) <= seconds:
                        lo = mid
                    else:
                        hi = mid - 1
                total_layers += lo
                if total_layers >= mountainHeight:
                    return True
            return total_layers >= mountainHeight

        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
