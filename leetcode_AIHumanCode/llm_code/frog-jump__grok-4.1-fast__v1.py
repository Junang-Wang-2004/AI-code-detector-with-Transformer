from collections import deque

class Solution:
    def canCross(self, stones):
        if len(stones) < 2 or stones[1] != 1:
            return False
        target = stones[-1]
        stone_set = set(stones)
        q = deque([(1, 1)])
        vis = set([(1, 1)])
        while q:
            pos, jump = q.popleft()
            if pos == target:
                return True
            for d in (-1, 0, 1):
                nj = jump + d
                if nj > 0:
                    np = pos + nj
                    state = (np, nj)
                    if np in stone_set and state not in vis:
                        vis.add(state)
                        q.append(state)
        return False
