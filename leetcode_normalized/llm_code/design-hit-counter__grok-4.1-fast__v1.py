from collections import deque

class C1:

    def __init__(self):
        self.times = deque()
        self.amounts = deque()
        self.total_hits = 0
        self.window_size = 300

    def _remove_old(self, a1):
        while self.times and self.times[0] <= a1 - self.window_size:
            self.total_hits -= self.amounts.popleft()
            self.times.popleft()

    def hit(self, a1):
        self._remove_old(a1)
        if self.times and self.times[-1] == a1:
            self.amounts[-1] += 1
        else:
            self.times.append(a1)
            self.amounts.append(1)
        self.total_hits += 1

    def getHits(self, a1):
        self._remove_old(a1)
        return self.total_hits
