import heapq

class Matrix3D:
    def __init__(self, n):
        self.dim = n
        self.cells = set()
        self.slices = [0] * n
        self.pq = []
        heapq.heappush(self.pq, (0, -(n - 1)))

    def setCell(self, x, y, z):
        pos = (x, y, z)
        if pos in self.cells:
            return
        self.cells.add(pos)
        self.slices[x] += 1
        heapq.heappush(self.pq, (-self.slices[x], -x))

    def unsetCell(self, x, y, z):
        pos = (x, y, z)
        if pos not in self.cells:
            return
        self.cells.remove(pos)
        self.slices[x] -= 1
        heapq.heappush(self.pq, (-self.slices[x], -x))

    def largestMatrix(self):
        while self.pq:
            neg_cnt, neg_idx = self.pq[0]
            idx = -neg_idx
            cnt = -neg_cnt
            if cnt == self.slices[idx]:
                return idx
            heapq.heappop(self.pq)
        return self.dim - 1
