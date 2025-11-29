import heapq


class AuthenticationManager:

    def __init__(self, timeToLive):
        self.ttl = timeToLive
        self.token_expiry = {}
        self.min_heap = []

    def _cleanup(self, currentTime):
        while self.min_heap and self.min_heap[0][0] <= currentTime:
            exp_time, t_id = heapq.heappop(self.min_heap)
            if t_id in self.token_expiry and self.token_expiry[t_id] == exp_time:
                del self.token_expiry[t_id]

    def generate(self, tokenId, currentTime):
        self._cleanup(currentTime)
        exp_time = currentTime + self.ttl
        self.token_expiry[tokenId] = exp_time
        heapq.heappush(self.min_heap, (exp_time, tokenId))

    def renew(self, tokenId, currentTime):
        self._cleanup(currentTime)
        if tokenId in self.token_expiry:
            exp_time = currentTime + self.ttl
            self.token_expiry[tokenId] = exp_time
            heapq.heappush(self.min_heap, (exp_time, tokenId))

    def countUnexpiredTokens(self, currentTime):
        self._cleanup(currentTime)
        return len(self.token_expiry)
