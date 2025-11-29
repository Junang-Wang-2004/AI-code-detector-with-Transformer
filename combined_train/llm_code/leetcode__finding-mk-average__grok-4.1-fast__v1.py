import collections
from sortedcontainers import SortedList

class C1:

    def __init__(self, a1: int, a2: int):
        self.m_val = a1
        self.k_val = a2
        self.elements_queue = collections.deque()
        self.ordered_list = SortedList()
        self.overall_sum = 0
        self.smallest_k_sum = 0
        self.largest_k_sum = 0

    def addElement(self, a1: int) -> None:
        if len(self.elements_queue) == self.m_val:
            v1 = self.elements_queue.popleft()
            self._handle_removal(v1)
        self.elements_queue.append(a1)
        self._handle_insertion(a1)

    def calculateMKAverage(self) -> int:
        if len(self.ordered_list) < self.m_val:
            return -1
        v1 = self.overall_sum - self.smallest_k_sum - self.largest_k_sum
        return v1 // (self.m_val - 2 * self.k_val)

    def _handle_insertion(self, a1: int) -> None:
        self.overall_sum += a1
        v1 = self.ordered_list.bisect_left(a1)
        v2 = len(self.ordered_list)
        if v1 < self.k_val:
            self.smallest_k_sum += a1
            if v2 >= self.k_val:
                self.smallest_k_sum -= self.ordered_list[self.k_val - 1]
        if v1 > v2 - self.k_val:
            self.largest_k_sum += a1
            if v2 >= self.k_val:
                self.largest_k_sum -= self.ordered_list[v2 - self.k_val]
        self.ordered_list.add(a1)

    def _handle_removal(self, a1: int) -> None:
        self.overall_sum -= a1
        v1 = self.ordered_list.index(a1)
        v2 = len(self.ordered_list)
        if v1 < self.k_val:
            self.smallest_k_sum -= a1
            self.smallest_k_sum += self.ordered_list[self.k_val]
        elif v1 > v2 - 1 - self.k_val:
            self.largest_k_sum -= a1
            self.largest_k_sum += self.ordered_list[v2 - self.k_val - 1]
        self.ordered_list.remove(a1)
