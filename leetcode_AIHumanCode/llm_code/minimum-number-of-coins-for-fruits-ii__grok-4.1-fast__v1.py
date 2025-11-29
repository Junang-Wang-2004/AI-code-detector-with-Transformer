import heapq

class Solution(object):
    def minimumCoins(self, prices):
        n = len(prices)
        mincost = [float('inf')] * (n + 1)
        mincost[0] = 0
        heap = []
        for idx in range(n):
            heapq.heappush(heap, (mincost[idx] + prices[idx], idx))
            start = idx // 2
            while heap and heap[0][1] < start:
                heapq.heappop(heap)
            mincost[idx + 1] = heap[0][0]
        return mincost[n]
