from collections import deque

class HitCounter:

    def __init__(self):
        self.times = deque()
        self.amounts = deque()
        self.total_hits = 0
        self.window_size = 300

    def _remove_old(self, current_time):
        while self.times and self.times[0] <= current_time - self.window_size:
            self.total_hits -= self.amounts.popleft()
            self.times.popleft()

    def hit(self, current_time):
        self._remove_old(current_time)
        if self.times and self.times[-1] == current_time:
            self.amounts[-1] += 1
        else:
            self.times.append(current_time)
            self.amounts.append(1)
        self.total_hits += 1

    def getHits(self, current_time):
        self._remove_old(current_time)
        return self.total_hits
