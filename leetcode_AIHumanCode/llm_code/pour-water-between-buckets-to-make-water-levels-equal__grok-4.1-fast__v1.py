class Solution:
    def equalizeWater(self, buckets, loss):
        eff = (100 - loss) / 100
        def feasible(tgt):
            excess = sum(max(b - tgt, 0) for b in buckets)
            deficit = sum(max(tgt - b, 0) for b in buckets)
            return excess * eff >= deficit
        lo = min(buckets)
        hi = sum(buckets) / len(buckets)
        while hi - lo > 1e-9:
            mid = (lo + hi) / 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid
        return lo
