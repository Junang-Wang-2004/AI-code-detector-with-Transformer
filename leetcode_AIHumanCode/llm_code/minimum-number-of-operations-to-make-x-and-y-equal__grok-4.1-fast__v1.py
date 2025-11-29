from collections import deque

class Solution:
    def minimumOperationsToMakeEqual(self, x, y):
        if x == y:
            return 0
        if y > x:
            return y - x
        upper = x + (x - y)
        dist = {x: 0}
        q = deque([x])
        while q:
            curr = q.popleft()
            if curr == y:
                return dist[curr]
            for nxt in (curr - 1, curr + 1):
                if 0 <= nxt <= upper and nxt not in dist:
                    dist[nxt] = dist[curr] + 1
                    q.append(nxt)
            for divisor in (5, 11):
                if curr % divisor == 0:
                    nxt = curr // divisor
                    if 0 <= nxt <= upper and nxt not in dist:
                        dist[nxt] = dist[curr] + 1
                        q.append(nxt)
        return -1
