from collections import deque
from typing import List, Tuple

class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        spos = [0] * (n + 1)
        for i in range(n):
            spos[i + 1] = spos[i] + nums[i]
        scst = [0] * (n + 1)
        for i in range(n):
            scst[i + 1] = scst[i] + cost[i]
        dq: deque[Tuple[int, int]] = deque()
        cdp = 0

        def evl(line: Tuple[int, int], xpos: int) -> int:
            return line[0] * xpos + line[1]

        def bd(l0: Tuple[int, int], l1: Tuple[int, int], l2: Tuple[int, int]) -> bool:
            return (l1[1] - l0[1]) * (l2[0] - l1[0]) >= (l2[1] - l1[1]) * (l1[0] - l0[0])

        for idx in range(n - 1, -1, -1):
            slp = spos[idx + 1]
            btc = - (cdp + spos[idx + 1] * scst[idx + 1])
            lnw = (slp, btc)
            while len(dq) >= 2 and bd(dq[-2], dq[-1], lnw):
                dq.pop()
            dq.append(lnw)
            qx = scst[idx]
            while len(dq) >= 2 and evl(dq[0], qx) >= evl(dq[1], qx):
                dq.popleft()
            bval = evl(dq[0], qx)
            cdp = -bval + k * (scst[n] - scst[idx])
        return cdp
