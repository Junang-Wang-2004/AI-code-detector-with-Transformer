import collections
import heapq

class FileSharing:
    def __init__(self, m):
        self.participants = {}
        self.chunk_holders = collections.defaultdict(set)
        self.available_ids = []
        self.current_id = 1

    def join(self, initial_chunks):
        if self.available_ids:
            pid = heapq.heappop(self.available_ids)
        else:
            pid = self.current_id
            self.current_id += 1
        self.participants[pid] = set(initial_chunks)
        for ch in initial_chunks:
            self.chunk_holders[ch].add(pid)
        return pid

    def leave(self, pid):
        if pid not in self.participants:
            return
        held_chunks = self.participants[pid]
        for ch in held_chunks:
            self.chunk_holders[ch].discard(pid)
        del self.participants[pid]
        heapq.heappush(self.available_ids, pid)

    def request(self, pid, ch):
        holders = sorted(self.chunk_holders[ch])
        if not holders:
            return None
        self.participants[pid].add(ch)
        self.chunk_holders[ch].add(pid)
        return holders
