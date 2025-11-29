import heapq

class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        available = []
        candidates = []
        for req, gain in zip(Capital, Profits):
            heapq.heappush(candidates, (req, gain))
        funds = W
        for _ in range(k):
            while candidates and candidates[0][0] <= funds:
                _, gain = heapq.heappop(candidates)
                heapq.heappush(available, -gain)
            if available:
                funds -= heapq.heappop(available)
        return funds
