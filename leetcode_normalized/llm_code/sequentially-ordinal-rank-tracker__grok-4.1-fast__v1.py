import heapq

class C1:

    def __init__(self):
        self.top = []
        self.bottom = []
        self.idx = 0
        self.tick = 0

    def _reverse_str(self, a1):
        return ''.join((chr(ord('a') + ord('z') - ord(c)) for v1 in a1))

    def add(self, a1, a2):
        self.tick += 1
        v1 = self._reverse_str(a1)
        v2 = (a2, v1, self.tick)
        v3 = (-a2, a1, self.tick)
        v4 = True
        if self.top:
            v5, v6, v7 = self.top[0]
            v8 = self._reverse_str(v6)
            v9 = (-v5, v8)
            v10 = (-a2, a1)
            v4 = v10 <= v9
        if v4:
            heapq.heappush(self.top, v2)
        else:
            heapq.heappush(self.bottom, v3)
        while len(self.top) > self.idx:
            v11, v12, v13 = heapq.heappop(self.top)
            v14 = self._reverse_str(v12)
            heapq.heappush(self.bottom, (-v11, v14, v13))

    def get(self):
        self.idx += 1
        while len(self.top) < self.idx and self.bottom:
            v1, v2, v3 = heapq.heappop(self.bottom)
            v4 = self._reverse_str(v2)
            heapq.heappush(self.top, (-v1, v4, v3))
        v5, v6, v7 = self.top[0]
        return self._reverse_str(v6)
