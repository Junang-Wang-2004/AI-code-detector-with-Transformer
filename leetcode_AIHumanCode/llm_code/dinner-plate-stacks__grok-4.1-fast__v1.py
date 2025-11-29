import heapq

class DinnerPlates:

    def __init__(self, capacity):
        self.plates = []
        self.limit = capacity
        self.free_slots = []

    def push(self, val):
        while self.free_slots and self.free_slots[0] >= len(self.plates):
            heapq.heappop(self.free_slots)
        if self.free_slots:
            pos = heapq.heappop(self.free_slots)
            self.plates[pos].append(val)
        else:
            if not self.plates or len(self.plates[-1]) == self.limit:
                self.plates.append([])
            self.plates[-1].append(val)

    def pop(self):
        while self.plates and not self.plates[-1]:
            self.plates.pop()
        return self.plates[-1].pop() if self.plates else -1

    def popAtStack(self, idx):
        if idx >= len(self.plates) or not self.plates[idx]:
            return -1
        val = self.plates[idx].pop()
        heapq.heappush(self.free_slots, idx)
        return val
