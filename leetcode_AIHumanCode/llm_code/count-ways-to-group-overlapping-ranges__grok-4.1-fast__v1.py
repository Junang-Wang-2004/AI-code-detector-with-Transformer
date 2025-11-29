class Solution:
    def countWays(self, ranges):
        MOD = 10**9 + 7
        ranges.sort()
        merged = []
        for seg in ranges:
            if not merged or seg[0] > merged[-1][1]:
                merged.append(seg)
            else:
                merged[-1][1] = max(merged[-1][1], seg[1])
        return pow(2, len(merged), MOD)
