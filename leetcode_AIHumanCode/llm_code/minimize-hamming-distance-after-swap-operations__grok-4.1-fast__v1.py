import collections
from collections import deque

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        graph = [[] for _ in range(n)]
        for a, b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)
        seen = [False] * n
        distance = 0
        for start in range(n):
            if seen[start]:
                continue
            positions = []
            queue = deque([start])
            seen[start] = True
            while queue:
                curr = queue.popleft()
                positions.append(curr)
                for neigh in graph[curr]:
                    if not seen[neigh]:
                        seen[neigh] = True
                        queue.append(neigh)
            src_freq = collections.Counter(source[i] for i in positions)
            tgt_freq = collections.Counter(target[i] for i in positions)
            excess = src_freq - tgt_freq
            distance += sum(excess.values())
        return distance
