from collections import deque
from typing import List

INF = 10**20

class Solution:
    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        robots.sort()
        factories.sort(key=lambda x: x[0])
        n = len(robots)
        dp_prev = [INF] * (n + 1)
        dp_prev[0] = 0
        for pos, cap in factories:
            cum = [0] * (n + 1)
            for i in range(1, n + 1):
                cum[i] = cum[i - 1] + abs(robots[i - 1] - pos)
            dp_curr = [INF] * (n + 1)
            dp_curr[0] = 0
            dq = deque()
            dq.append(0)
            for j in range(1, n + 1):
                while dq and dq[0] < j - cap:
                    dq.popleft()
                if dq:
                    min_val = dp_prev[dq[0]] - cum[dq[0]] + cum[j]
                    dp_curr[j] = min(dp_curr[j], min_val)
                dp_curr[j] = min(dp_curr[j], dp_prev[j])
                val_j = dp_prev[j] - cum[j]
                while dq and dp_prev[dq[-1]] - cum[dq[-1]] >= val_j:
                    dq.pop()
                dq.append(j)
            dp_prev = dp_curr
        return dp_prev[n]
