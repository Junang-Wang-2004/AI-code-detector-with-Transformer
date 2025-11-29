import math

class Solution:
    def minmaxGasDist(self, stations, K):
        def feasible(max_gap):
            req = 0
            for i in range(len(stations) - 1):
                gap = stations[i + 1] - stations[i]
                req += math.ceil(gap / max_gap) - 1
            return req <= K

        lo, hi = 0.0, stations[-1] - stations[0]
        for _ in range(100):
            mid = (lo + hi) / 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid
        return lo
