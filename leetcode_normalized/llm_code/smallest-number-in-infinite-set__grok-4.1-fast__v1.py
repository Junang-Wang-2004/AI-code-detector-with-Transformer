import heapq

class C1:

    def __init__(self):
        self.frontier = 1
        self.minheap = []
        self.tracked = set()

    def popSmallest(self):
        if self.minheap:
            v1 = heapq.heappop(self.minheap)
            self.tracked.remove(v1)
            return v1
        else:
            v1 = self.frontier
            self.frontier += 1
            return v1

    def addBack(self, a1):
        if a1 < self.frontier:
            if a1 not in self.tracked:
                self.tracked.add(a1)
                heapq.heappush(self.minheap, a1)
