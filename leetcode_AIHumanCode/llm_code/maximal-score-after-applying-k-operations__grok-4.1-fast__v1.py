import heapq

class Solution:
    def maxKelements(self, nums, k):
        pq = [-x for x in nums]
        heapq.heapify(pq)
        ans = 0
        remaining = k
        while remaining > 0:
            if not pq:
                break
            maximum = -heapq.heappop(pq)
            ans += maximum
            successor = (maximum + 2) // 3
            if successor > 0:
                heapq.heappush(pq, -successor)
            remaining -= 1
        return ans
