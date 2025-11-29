class Solution:
    def minimumTime(self, bus_times, total_needed):
        def sufficient(duration):
            trips = 0
            for t in bus_times:
                trips += duration // t
                if trips >= total_needed:
                    return True
            return trips >= total_needed

        lo = 1
        hi = max(bus_times) * total_needed
        while lo < hi:
            md = (lo + hi) // 2
            if sufficient(md):
                hi = md
            else:
                lo = md + 1
        return lo
