import heapq

class C1:

    def __init__(self, a1, a2):
        self.capacity = a1
        self.pq = sorted(a2)[-a1:]
        heapq.heapify(self.pq)

    def add(self, a1):
        if len(self.pq) < self.capacity:
            heapq.heappush(self.pq, a1)
        elif a1 > self.pq[0]:
            heapq.heappop(self.pq)
            heapq.heappush(self.pq, a1)
        return self.pq[0]
