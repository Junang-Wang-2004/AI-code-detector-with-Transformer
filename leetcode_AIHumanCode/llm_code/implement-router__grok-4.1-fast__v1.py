import collections
from sortedcontainers import SortedList
from bisect import bisect_left

class Router:

    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.packet_queue = collections.deque()
        self.dest_index = collections.defaultdict(SortedList)

    def addPacket(self, origin, target, time):
        pkt_id = (time, origin)
        idx = self.dest_index[target]
        if pkt_id in idx:
            return False
        idx.add(pkt_id)
        if len(self.packet_queue) == self.buffer_size:
            prev_origin, prev_target, prev_time = self.packet_queue.popleft()
            prev_id = (prev_time, prev_origin)
            self.dest_index[prev_target].remove(prev_id)
        self.packet_queue.append((origin, target, time))
        return True

    def forwardPacket(self):
        if not self.packet_queue:
            return []
        origin, target, time = self.packet_queue.popleft()
        pkt_id = (time, origin)
        self.dest_index[target].remove(pkt_id)
        return [origin, target, time]

    def getCount(self, target, low_time, high_time):
        idx = self.dest_index[target]
        return bisect_left(idx, (high_time + 1, 0)) - bisect_left(idx, (low_time, 0))
