import heapq

class C1:

    def __init__(self):
        self.smallest = []
        self.largest = []
        self.latest = 0

    def update(self, a1, a2):
        self.latest = a2
        heapq.heappush(self.smallest, a2)
        heapq.heappush(self.largest, -a2)

    def current(self):
        return self.latest

    def maximum(self):
        return -self.largest[0]

    def minimum(self):
        return self.smallest[0]
