import heapq

class Solution(object):
    def kSum(self, nums, k):
        max_sum = 0
        for num in nums:
            if num > 0:
                max_sum += num
        abs_sorted = []
        for num in nums:
            abs_sorted.append(abs(num))
        abs_sorted.sort()
        pq = []
        heapq.heappush(pq, (-max_sum, 0))
        count = 0
        while count < k:
            neg_val, idx = heapq.heappop(pq)
            current = -neg_val
            count += 1
            if idx < len(abs_sorted):
                next_current = current - abs_sorted[idx]
                heapq.heappush(pq, (-next_current, idx + 1))
                if idx > 0:
                    next_current2 = current + abs_sorted[idx - 1] - abs_sorted[idx]
                    heapq.heappush(pq, (-next_current2, idx + 1))
        return current
