class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        earnings = [0] * (n + 1)
        by_start = [[] for _ in range(n + 1)]
        for a, b, c in rides:
            by_start[a].append((b, c))
        for pos in range(1, n + 1):
            earnings[pos] = max(earnings[pos], earnings[pos - 1])
            for dest, val in by_start[pos]:
                gain = dest - pos + val
                earnings[dest] = max(earnings[dest], earnings[pos] + gain)
        return earnings[n]
