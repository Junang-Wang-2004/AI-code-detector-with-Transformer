class Solution:
    def maximizeTheProfit(self, n, offers):
        buckets = [[] for _ in range(n)]
        for start, end, profit in offers:
            buckets[end].append((start, profit))
        values = [0] * (n + 1)
        for i in range(n):
            candidate = values[i]
            for j, p in buckets[i]:
                candidate = max(candidate, values[j] + p)
            values[i + 1] = candidate
        return values[-1]
