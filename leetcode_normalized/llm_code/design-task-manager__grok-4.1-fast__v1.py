import heapq

class C1:

    def __init__(self, a1):
        self.active_tasks = {}
        self.min_heap = []
        for v1, v2, v3 in a1:
            self.add(v1, v2, v3)

    def add(self, a1, a2, a3):
        heapq.heappush(self.min_heap, (-a3, -a2, -a1))
        self.active_tasks[a2] = (a1, a3)

    def edit(self, a1, a2):
        if a1 in self.active_tasks:
            v1 = self.active_tasks[a1][0]
            self.rmv(a1)
            self.add(v1, a1, a2)

    def rmv(self, a1):
        self.active_tasks.pop(a1, None)

    def execTop(self):
        while self.min_heap:
            v1, v2, v3 = self.min_heap[0]
            v4 = -v2
            v5 = -v1
            if v4 in self.active_tasks and self.active_tasks[v4][1] == v5:
                heapq.heappop(self.min_heap)
                v6 = -v3
                self.rmv(v4)
                return v6
            heapq.heappop(self.min_heap)
        return -1
