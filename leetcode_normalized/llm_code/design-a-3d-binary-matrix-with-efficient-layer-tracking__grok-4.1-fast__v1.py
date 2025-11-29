import heapq

class C1:

    def __init__(self, a1):
        self.dim = a1
        self.cells = set()
        self.slices = [0] * a1
        self.pq = []
        heapq.heappush(self.pq, (0, -(a1 - 1)))

    def setCell(self, a1, a2, a3):
        v1 = (a1, a2, a3)
        if v1 in self.cells:
            return
        self.cells.add(v1)
        self.slices[a1] += 1
        heapq.heappush(self.pq, (-self.slices[a1], -a1))

    def unsetCell(self, a1, a2, a3):
        v1 = (a1, a2, a3)
        if v1 not in self.cells:
            return
        self.cells.remove(v1)
        self.slices[a1] -= 1
        heapq.heappush(self.pq, (-self.slices[a1], -a1))

    def largestMatrix(self):
        while self.pq:
            v1, v2 = self.pq[0]
            v3 = -v2
            v4 = -v1
            if v4 == self.slices[v3]:
                return v3
            heapq.heappop(self.pq)
        return self.dim - 1
