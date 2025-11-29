import heapq

class C1(object):

    def __init__(self, a1):
        self.N = a1
        self.prev_neighbor = {a1: -1}
        self.next_neighbor = {-1: a1}
        self.maxgaps = []
        heapq.heappush(self.maxgaps, (-a1, -1, a1))

    def _gap_size(self, a1, a2):
        if a1 == -1 or a2 == self.N:
            return a2 - a1 - 1
        return (a2 - a1) // 2

    def seat(self):
        while self.maxgaps and (not (self.next_neighbor[self.maxgaps[0][1]] == self.maxgaps[0][2] and self.prev_neighbor[self.maxgaps[0][2]] == self.maxgaps[0][1])):
            heapq.heappop(self.maxgaps)
        v1, v2, v3 = heapq.heappop(self.maxgaps)
        if v2 == -1:
            v4 = 0
        elif v3 == self.N:
            v4 = self.N - 1
        else:
            v4 = (v2 + v3) // 2
        self.prev_neighbor[v4] = v2
        self.next_neighbor[v4] = v3
        self.next_neighbor[v2] = v4
        self.prev_neighbor[v3] = v4
        heapq.heappush(self.maxgaps, (-self._gap_size(v2, v4), v2, v4))
        heapq.heappush(self.maxgaps, (-self._gap_size(v4, v3), v4, v3))
        return v4

    def leave(self, a1):
        v1 = self.prev_neighbor[a1]
        v2 = self.next_neighbor[a1]
        self.next_neighbor[v1] = v2
        self.prev_neighbor[v2] = v1
        del self.prev_neighbor[a1]
        del self.next_neighbor[a1]
        heapq.heappush(self.maxgaps, (-self._gap_size(v1, v2), v1, v2))
