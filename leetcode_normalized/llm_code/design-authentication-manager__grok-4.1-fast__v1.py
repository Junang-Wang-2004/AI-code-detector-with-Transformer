import heapq

class C1:

    def __init__(self, a1):
        self.ttl = a1
        self.token_expiry = {}
        self.min_heap = []

    def _cleanup(self, a1):
        while self.min_heap and self.min_heap[0][0] <= a1:
            v1, v2 = heapq.heappop(self.min_heap)
            if v2 in self.token_expiry and self.token_expiry[v2] == v1:
                del self.token_expiry[v2]

    def generate(self, a1, a2):
        self._cleanup(a2)
        v1 = a2 + self.ttl
        self.token_expiry[a1] = v1
        heapq.heappush(self.min_heap, (v1, a1))

    def renew(self, a1, a2):
        self._cleanup(a2)
        if a1 in self.token_expiry:
            v1 = a2 + self.ttl
            self.token_expiry[a1] = v1
            heapq.heappush(self.min_heap, (v1, a1))

    def countUnexpiredTokens(self, a1):
        self._cleanup(a1)
        return len(self.token_expiry)
