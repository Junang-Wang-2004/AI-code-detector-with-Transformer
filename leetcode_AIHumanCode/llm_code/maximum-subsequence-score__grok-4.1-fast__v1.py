import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        n = len(nums1)
        indices = sorted(range(n), key=lambda i: -nums2[i])
        pq = []
        total = 0
        best = 0
        for i in indices:
            heapq.heappush(pq, nums1[i])
            total += nums1[i]
            if len(pq) > k:
                total -= heapq.heappop(pq)
            if len(pq) == k:
                best = max(best, total * nums2[i])
        return best
