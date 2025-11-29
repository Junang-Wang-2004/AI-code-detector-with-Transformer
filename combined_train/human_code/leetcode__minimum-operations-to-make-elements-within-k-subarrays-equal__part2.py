import heapq
import collections

class C1(object):

    def minOperations(self, a1, a2, a3):
        """
        """

        class LazyHeap(object):

            def __init__(self, a1):
                self.heap = []
                self.to_remove = collections.defaultdict(int)
                self.cnt = 0
                self.sign = a1

            def push(self, a1):
                heapq.heappush(self.heap, self.sign * a1)

            def full_remove(self):
                v1 = []
                for v2 in self.heap:
                    if v2 not in self.to_remove:
                        v1.append(v2)
                        continue
                    self.to_remove[v2] -= 1
                    if not self.to_remove[v2]:
                        del self.to_remove[v2]
                self.heap[:] = v1
                heapq.heapify(self.heap)

            def remove(self, a1):
                self.to_remove[self.sign * a1] += 1
                self.cnt += 1
                if self.cnt > len(self.heap) - self.cnt:
                    self.full_remove()
                    self.cnt = 0

            def pop(self):
                self.remove(self.top())

            def top(self):
                while self.heap and self.heap[0] in self.to_remove:
                    self.to_remove[self.heap[0]] -= 1
                    self.cnt -= 1
                    if self.to_remove[self.heap[0]] == 0:
                        del self.to_remove[self.heap[0]]
                    heapq.heappop(self.heap)
                return self.sign * self.heap[0]

            def __len__(self):
                return len(self.heap) - self.cnt

        class SlidingWindow(object):

            def __init__(self):
                self.left = LazyHeap(-1)
                self.right = LazyHeap(+1)
                self.total1 = self.total2 = 0

            def add(self, a1):
                if not self.left or a1 <= self.left.top():
                    self.left.push(a1)
                    self.total1 += a1
                else:
                    self.right.push(a1)
                    self.total2 += a1
                self.rebalance()

            def remove(self, a1):
                if a1 <= self.left.top():
                    self.left.remove(a1)
                    self.total1 -= a1
                else:
                    self.right.remove(a1)
                    self.total2 -= a1
                self.rebalance()

            def rebalance(self):
                if len(self.left) < len(self.right):
                    self.total2 -= self.right.top()
                    self.total1 += self.right.top()
                    self.left.push(self.right.top())
                    self.right.pop()
                elif len(self.left) > len(self.right) + 1:
                    self.total1 -= self.left.top()
                    self.total2 += self.left.top()
                    self.right.push(self.left.top())
                    self.left.pop()

            def median(self):
                return self.left.top()
        v1 = float('inf')
        v2 = SlidingWindow()
        v3 = [v1] * (len(a1) + 1)
        for v4 in range(len(a1)):
            if v4 - a2 >= 0:
                v2.remove(a1[v4 - a2])
            v2.add(a1[v4])
            if v4 >= a2 - 1:
                v3[v4 + 1] = v2.median() * len(v2.left) - v2.total1 + (v2.total2 - v2.median() * len(v2.right))
        v5 = [0] * (len(a1) + 1)
        for v4 in range(a3):
            v6 = [v1] * (len(a1) + 1)
            for v7 in range((v4 + 1) * a2, len(a1) + 1):
                v6[v7] = min(v6[v7 - 1], v5[v7 - a2] + v3[v7])
            v5 = v6
        return v5[-1]
