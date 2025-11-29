from collections import deque

class Solution:
    def numberOfNodes(self, n, queries):
        marks = [0] * (n + 1)
        for q in queries:
            marks[q] ^= 1
        total = 0
        queue = deque([(1, 0)])
        while queue:
            node, path_parity = queue.popleft()
            here_parity = path_parity ^ marks[node]
            total += here_parity
            left = 2 * node
            right = left + 1
            if left <= n:
                queue.append((left, here_parity))
            if right <= n:
                queue.append((right, here_parity))
        return total
