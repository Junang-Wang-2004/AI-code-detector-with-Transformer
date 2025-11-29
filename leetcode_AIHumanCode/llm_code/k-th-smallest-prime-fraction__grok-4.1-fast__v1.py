import heapq

class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        n = len(A)
        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (A[i] / A[n - 1], i, n - 1))
        cnt = 0
        while True:
            frac, x, y = heapq.heappop(pq)
            cnt += 1
            if cnt == K:
                return [A[x], A[y]]
            if y > x + 1:
                heapq.heappush(pq, (A[x] / A[y - 1], x, y - 1))
