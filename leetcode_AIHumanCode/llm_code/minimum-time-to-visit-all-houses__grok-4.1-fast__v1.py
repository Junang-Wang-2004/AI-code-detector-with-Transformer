class Solution(object):
    def minTotalTime(self, forward, backward, queries):
        n = len(forward)
        fwd = [0] * (2 * n + 1)
        for i in range(2 * n):
            fwd[i + 1] = fwd[i] + forward[i % n]
        bwd = [0] * (2 * n + 1)
        for i in range(2 * n):
            bwd[i + 1] = bwd[i] + backward[i % n]
        total = 0
        cur = 0
        for nxt in queries:
            fwd_cost = fwd[nxt + n if nxt < cur else nxt] - fwd[cur]
            bwd_cost = bwd[cur + n + 1 if cur < nxt else cur + 1] - bwd[nxt + 1]
            total += min(fwd_cost, bwd_cost)
            cur = nxt
        return total
