import heapq

class StockPrice:
    def __init__(self):
        self.smallest = []
        self.largest = []
        self.latest = 0

    def update(self, t, p):
        self.latest = p
        heapq.heappush(self.smallest, p)
        heapq.heappush(self.largest, -p)

    def current(self):
        return self.latest

    def maximum(self):
        return -self.largest[0]

    def minimum(self):
        return self.smallest[0]
