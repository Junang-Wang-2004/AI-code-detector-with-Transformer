import collections
from sortedcontainers import SortedList
from bisect import bisect_left

class C1:

    def __init__(self, a1):
        self.buffer_size = a1
        self.packet_queue = collections.deque()
        self.dest_index = collections.defaultdict(SortedList)

    def addPacket(self, a1, a2, a3):
        v1 = (a3, a1)
        v2 = self.dest_index[a2]
        if v1 in v2:
            return False
        v2.add(v1)
        if len(self.packet_queue) == self.buffer_size:
            v3, v4, v5 = self.packet_queue.popleft()
            v6 = (v5, v3)
            self.dest_index[v4].remove(v6)
        self.packet_queue.append((a1, a2, a3))
        return True

    def forwardPacket(self):
        if not self.packet_queue:
            return []
        v1, v2, v3 = self.packet_queue.popleft()
        v4 = (v3, v1)
        self.dest_index[v2].remove(v4)
        return [v1, v2, v3]

    def getCount(self, a1, a2, a3):
        v1 = self.dest_index[a1]
        return bisect_left(v1, (a3 + 1, 0)) - bisect_left(v1, (a2, 0))
