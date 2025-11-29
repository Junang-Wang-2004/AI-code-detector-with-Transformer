import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.frontier = 1
        self.minheap = []
        self.tracked = set()

    def popSmallest(self):
        if self.minheap:
            smallest = heapq.heappop(self.minheap)
            self.tracked.remove(smallest)
            return smallest
        else:
            smallest = self.frontier
            self.frontier += 1
            return smallest

    def addBack(self, value):
        if value < self.frontier:
            if value not in self.tracked:
                self.tracked.add(value)
                heapq.heappush(self.minheap, value)
