import heapq

class NumberContainers:
    def __init__(self):
        self.nums = {}
        self.heaps = {}

    def change(self, index, number):
        old = self.nums.get(index, None)
        self.nums[index] = number
        if old != number:
            if number not in self.heaps:
                self.heaps[number] = []
            heapq.heappush(self.heaps[number], index)

    def find(self, number):
        if number not in self.heaps:
            return -1
        h = self.heaps[number]
        while h and self.nums[h[0]] != number:
            heapq.heappop(h)
        return h[0] if h else -1
