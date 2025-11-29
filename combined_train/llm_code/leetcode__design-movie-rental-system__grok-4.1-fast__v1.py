import collections
import heapq

class C1:

    def __init__(self, a1, a2):
        self.prices = {}
        self.avail_heaps = collections.defaultdict(list)
        self.rented_items = set()
        self.rented_heap = []
        for v1, v2, v3 in a2:
            v4 = (v1, v2)
            self.prices[v4] = v3
            heapq.heappush(self.avail_heaps[v2], (v3, v1))

    def search(self, a1):
        v1 = self.avail_heaps[a1]
        v2 = []
        v3 = []
        while len(v2) < 5 and v1:
            v4, v5 = heapq.heappop(v1)
            v6 = (v5, a1)
            if v6 not in self.rented_items:
                v2.append(v5)
                v3.append((v4, v5))
        for v7 in v3:
            heapq.heappush(v1, v7)
        return v2

    def rent(self, a1, a2):
        v1 = (a1, a2)
        v2 = self.prices[v1]
        self.rented_items.add(v1)
        heapq.heappush(self.rented_heap, (v2, a1, a2))

    def drop(self, a1, a2):
        v1 = (a1, a2)
        self.rented_items.remove(v1)

    def report(self):
        v1 = self.rented_heap
        v2 = []
        v3 = []
        while len(v2) < 5 and v1:
            v4, v5, v6 = heapq.heappop(v1)
            v7 = (v5, v6)
            if v7 in self.rented_items:
                v2.append([v5, v6])
                v3.append((v4, v5, v6))
        for v8 in v3:
            heapq.heappush(v1, v8)
        return v2
