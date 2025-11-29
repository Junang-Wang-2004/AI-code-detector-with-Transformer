import heapq

class C1:

    def __init__(self, a1):
        self.plates = []
        self.limit = a1
        self.free_slots = []

    def push(self, a1):
        while self.free_slots and self.free_slots[0] >= len(self.plates):
            heapq.heappop(self.free_slots)
        if self.free_slots:
            v1 = heapq.heappop(self.free_slots)
            self.plates[v1].append(a1)
        else:
            if not self.plates or len(self.plates[-1]) == self.limit:
                self.plates.append([])
            self.plates[-1].append(a1)

    def pop(self):
        while self.plates and (not self.plates[-1]):
            self.plates.pop()
        return self.plates[-1].pop() if self.plates else -1

    def popAtStack(self, a1):
        if a1 >= len(self.plates) or not self.plates[a1]:
            return -1
        v1 = self.plates[a1].pop()
        heapq.heappush(self.free_slots, a1)
        return v1
