class Solution:
    def findMaximalUncoveredRanges(self, n, ranges):
        segments = sorted(ranges)
        merged = []
        for a, b in segments:
            if not merged or merged[-1][1] < a:
                merged.append([a, b])
            else:
                merged[-1][1] = max(merged[-1][1], b)
        gaps = []
        last = -1
        for x, y in merged:
            if last + 1 < x:
                gaps.append([last + 1, x - 1])
            last = max(last, y)
        if last + 1 < n:
            gaps.append([last + 1, n - 1])
        return gaps
