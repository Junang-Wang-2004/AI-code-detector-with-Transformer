from heapq import heappush, heappop

class C1:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, a1):
        heappush(self.left, -a1)
        if self.right and -self.left[0] > self.right[0]:
            heappush(self.right, -heappop(self.left))
        if len(self.left) > len(self.right) + 1:
            heappush(self.right, -heappop(self.left))
        if len(self.right) > len(self.left):
            heappush(self.left, -heappop(self.right))

    def findMedian(self):
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        return -self.left[0]
