import collections
import heapq

class C1:

    def __init__(self, a1):
        self.participants = {}
        self.chunk_holders = collections.defaultdict(set)
        self.available_ids = []
        self.current_id = 1

    def join(self, a1):
        if self.available_ids:
            v1 = heapq.heappop(self.available_ids)
        else:
            v1 = self.current_id
            self.current_id += 1
        self.participants[v1] = set(a1)
        for v2 in a1:
            self.chunk_holders[v2].add(v1)
        return v1

    def leave(self, a1):
        if a1 not in self.participants:
            return
        v1 = self.participants[a1]
        for v2 in v1:
            self.chunk_holders[v2].discard(a1)
        del self.participants[a1]
        heapq.heappush(self.available_ids, a1)

    def request(self, a1, a2):
        v1 = sorted(self.chunk_holders[a2])
        if not v1:
            return None
        self.participants[a1].add(a2)
        self.chunk_holders[a2].add(a1)
        return v1
