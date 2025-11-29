import heapq
import collections

class C1:

    def minOperations(self, a1, a2, a3):
        v1 = len(a1)
        v2 = float('inf')

        class WindowMedian:

            def __init__(self):
                self.max_heap = []
                self.min_heap = []
                self.left_sum = 0
                self.right_sum = 0
                self.left_delays = collections.Counter()
                self.right_delays = collections.Counter()
                self.left_delay_cnt = 0
                self.right_delay_cnt = 0

            def _clean_max(self):
                while self.max_heap and (-self.max_heap[0] in self.left_delays and self.left_delays[-self.max_heap[0]] > 0):
                    v1 = -heapq.heappop(self.max_heap)
                    self.left_delays[v1] -= 1
                    self.left_delay_cnt -= 1

            def _clean_min(self):
                while self.min_heap and (self.min_heap[0] in self.right_delays and self.right_delays[self.min_heap[0]] > 0):
                    v1 = heapq.heappop(self.min_heap)
                    self.right_delays[v1] -= 1
                    self.right_delay_cnt -= 1

            def median(self):
                self._clean_max()
                return -self.max_heap[0]

            def left_size(self):
                self._clean_max()
                return len(self.max_heap) - self.left_delay_cnt

            def right_size(self):
                self._clean_min()
                return len(self.min_heap) - self.right_delay_cnt

            def add(self, a1):
                v1 = self.median() if self.max_heap else float('-inf')
                if a1 <= v1:
                    heapq.heappush(self.max_heap, -a1)
                    self.left_sum += a1
                else:
                    heapq.heappush(self.min_heap, a1)
                    self.right_sum += a1
                self._rebalance()

            def remove(self, a1):
                v1 = self.median() if self.max_heap else float('inf')
                if a1 <= v1:
                    self.left_delays[a1] += 1
                    self.left_delay_cnt += 1
                    self.left_sum -= a1
                else:
                    self.right_delays[a1] += 1
                    self.right_delay_cnt += 1
                    self.right_sum -= a1
                self._rebalance()

            def _rebalance(self):
                v1 = self.left_size()
                v2 = self.right_size()
                if v1 < v2:
                    self._clean_min()
                    if self.min_heap:
                        v3 = self.min_heap[0]
                        self.right_sum -= v3
                        self.left_sum += v3
                        heapq.heappush(self.max_heap, -v3)
                        heapq.heappop(self.min_heap)
                elif v1 > v2 + 1:
                    self._clean_max()
                    if self.max_heap:
                        v3 = -self.max_heap[0]
                        self.left_sum -= v3
                        self.right_sum += v3
                        heapq.heappush(self.min_heap, v3)
                        heapq.heappop(self.max_heap)
        v3 = WindowMedian()
        v4 = [v2] * (v1 + 1)
        for v5 in range(v1):
            if v5 >= a2:
                v3.remove(a1[v5 - a2])
            v3.add(a1[v5])
            if v5 >= a2 - 1:
                v6 = v3.median()
                v7 = v3.left_size()
                v8 = v3.right_size()
                v4[v5 + 1] = v6 * v7 - v3.left_sum + v3.right_sum - v6 * v8
        v9 = [0] * (v1 + 1)
        for v10 in range(1, a3 + 1):
            v11 = [v2] * (v1 + 1)
            v12 = v10 * a2
            for v13 in range(v12, v1 + 1):
                v14 = v11[v13 - 1] if v13 - 1 >= 0 else v2
                v15 = v9[v13 - a2] + v4[v13] if v13 - a2 >= 0 else v2
                v11[v13] = min(v14, v15)
            v9 = v11
        return v9[v1]
