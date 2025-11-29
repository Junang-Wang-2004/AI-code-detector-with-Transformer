class Solution:
    def minSpeedOnTime(self, dist, hour):
        def time_needed(speed):
            t = sum(d // speed + (1 if d % speed > 0 else 0) for d in dist[:-1]) + dist[-1] / speed
            return t

        max_speed = 10000000
        if time_needed(max_speed) > hour:
            return -1

        lo, hi = 1, max_speed
        while lo < hi:
            mid = (lo + hi) // 2
            if time_needed(mid) <= hour:
                hi = mid
            else:
                lo = mid + 1
        return lo
