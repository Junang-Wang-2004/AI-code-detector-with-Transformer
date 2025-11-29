import heapq
import collections

class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        INF = float('inf')
        class WindowMedian:
            def __init__(self):
                self.max_heap = []  # left half, negated for max heap
                self.min_heap = []  # right half
                self.left_sum = 0
                self.right_sum = 0
                self.left_delays = collections.Counter()
                self.right_delays = collections.Counter()
                self.left_delay_cnt = 0
                self.right_delay_cnt = 0

            def _clean_max(self):
                while self.max_heap and (-self.max_heap[0] in self.left_delays and
                                          self.left_delays[-self.max_heap[0]] > 0):
                    val = -heapq.heappop(self.max_heap)
                    self.left_delays[val] -= 1
                    self.left_delay_cnt -= 1

            def _clean_min(self):
                while self.min_heap and (self.min_heap[0] in self.right_delays and
                                         self.right_delays[self.min_heap[0]] > 0):
                    val = heapq.heappop(self.min_heap)
                    self.right_delays[val] -= 1
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

            def add(self, val):
                med = self.median() if self.max_heap else float('-inf')
                if val <= med:
                    heapq.heappush(self.max_heap, -val)
                    self.left_sum += val
                else:
                    heapq.heappush(self.min_heap, val)
                    self.right_sum += val
                self._rebalance()

            def remove(self, val):
                med = self.median() if self.max_heap else float('inf')
                if val <= med:
                    self.left_delays[val] += 1
                    self.left_delay_cnt += 1
                    self.left_sum -= val
                else:
                    self.right_delays[val] += 1
                    self.right_delay_cnt += 1
                    self.right_sum -= val
                self._rebalance()

            def _rebalance(self):
                lsz = self.left_size()
                rsz = self.right_size()
                if lsz < rsz:
                    self._clean_min()
                    if self.min_heap:
                        v = self.min_heap[0]
                        self.right_sum -= v
                        self.left_sum += v
                        heapq.heappush(self.max_heap, -v)
                        heapq.heappop(self.min_heap)
                elif lsz > rsz + 1:
                    self._clean_max()
                    if self.max_heap:
                        v = -self.max_heap[0]
                        self.left_sum -= v
                        self.right_sum += v
                        heapq.heappush(self.min_heap, v)
                        heapq.heappop(self.max_heap)

        window = WindowMedian()
        costs = [INF] * (n + 1)
        for i in range(n):
            if i >= x:
                window.remove(nums[i - x])
            window.add(nums[i])
            if i >= x - 1:
                m = window.median()
                ls = window.left_size()
                rs = window.right_size()
                costs[i + 1] = m * ls - window.left_sum + window.right_sum - m * rs

        dp = [0] * (n + 1)
        for ops in range(1, k + 1):
            new_dp = [INF] * (n + 1)
            st = ops * x
            for j in range(st, n + 1):
                prev_free = new_dp[j - 1] if j - 1 >= 0 else INF
                prev_seg = dp[j - x] + costs[j] if j - x >= 0 else INF
                new_dp[j] = min(prev_free, prev_seg)
            dp = new_dp
        return dp[n]
