from sortedcontainers import SortedList

class C1(object):

    def minOperations(self, a1, a2, a3):
        """
        """

        class SlidingWindow(object):

            def __init__(self):
                self.left = SortedList()
                self.right = SortedList()
                self.total1 = self.total2 = 0

            def add(self, a1):
                if not self.left or a1 <= self.left[-1]:
                    self.left.add(a1)
                    self.total1 += a1
                else:
                    self.right.add(a1)
                    self.total2 += a1
                self.rebalance()

            def remove(self, a1):
                if a1 <= self.left[-1]:
                    self.left.remove(a1)
                    self.total1 -= a1
                else:
                    self.right.remove(a1)
                    self.total2 -= a1
                self.rebalance()

            def rebalance(self):
                if len(self.left) < len(self.right):
                    self.total2 -= self.right[0]
                    self.total1 += self.right[0]
                    self.left.add(self.right[0])
                    self.right.pop(0)
                elif len(self.left) > len(self.right) + 1:
                    self.total1 -= self.left[-1]
                    self.total2 += self.left[-1]
                    self.right.add(self.left[-1])
                    self.left.pop()

            def median(self):
                return self.left[-1]
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
