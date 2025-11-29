import heapq

class C1:

    def __init__(self):
        self.nums = {}
        self.heaps = {}

    def change(self, a1, a2):
        v1 = self.nums.get(a1, None)
        self.nums[a1] = a2
        if v1 != a2:
            if a2 not in self.heaps:
                self.heaps[a2] = []
            heapq.heappush(self.heaps[a2], a1)

    def find(self, a1):
        if a1 not in self.heaps:
            return -1
        v1 = self.heaps[a1]
        while v1 and self.nums[v1[0]] != a1:
            heapq.heappop(v1)
        return v1[0] if v1 else -1
