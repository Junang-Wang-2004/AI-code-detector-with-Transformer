import collections
from sortedcontainers import SortedList

class MKAverage:
    def __init__(self, m: int, k: int):
        self.m_val = m
        self.k_val = k
        self.elements_queue = collections.deque()
        self.ordered_list = SortedList()
        self.overall_sum = 0
        self.smallest_k_sum = 0
        self.largest_k_sum = 0

    def addElement(self, num: int) -> None:
        if len(self.elements_queue) == self.m_val:
            leaving_num = self.elements_queue.popleft()
            self._handle_removal(leaving_num)
        self.elements_queue.append(num)
        self._handle_insertion(num)

    def calculateMKAverage(self) -> int:
        if len(self.ordered_list) < self.m_val:
            return -1
        mid_sum = (self.overall_sum - self.smallest_k_sum - self.largest_k_sum)
        return mid_sum // (self.m_val - 2 * self.k_val)

    def _handle_insertion(self, num: int) -> None:
        self.overall_sum += num
        insert_pos = self.ordered_list.bisect_left(num)
        curr_size = len(self.ordered_list)
        if insert_pos < self.k_val:
            self.smallest_k_sum += num
            if curr_size >= self.k_val:
                self.smallest_k_sum -= self.ordered_list[self.k_val - 1]
        if insert_pos > curr_size - self.k_val:
            self.largest_k_sum += num
            if curr_size >= self.k_val:
                self.largest_k_sum -= self.ordered_list[curr_size - self.k_val]
        self.ordered_list.add(num)

    def _handle_removal(self, num: int) -> None:
        self.overall_sum -= num
        remove_pos = self.ordered_list.index(num)
        curr_size = len(self.ordered_list)
        if remove_pos < self.k_val:
            self.smallest_k_sum -= num
            self.smallest_k_sum += self.ordered_list[self.k_val]
        elif remove_pos > curr_size - 1 - self.k_val:
            self.largest_k_sum -= num
            self.largest_k_sum += self.ordered_list[curr_size - self.k_val - 1]
        self.ordered_list.remove(num)
