import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.capacity = k
        self.pq = sorted(nums)[-k:]
        heapq.heapify(self.pq)

    def add(self, val):
        if len(self.pq) < self.capacity:
            heapq.heappush(self.pq, val)
        elif val > self.pq[0]:
            heapq.heappop(self.pq)
            heapq.heappush(self.pq, val)
        return self.pq[0]
