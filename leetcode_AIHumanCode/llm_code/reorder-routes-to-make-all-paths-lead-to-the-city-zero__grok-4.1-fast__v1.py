from collections import deque

class Solution:
    def minReorder(self, n, connections):
        adj = [[] for _ in range(n)]
        dirs = set()
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
            dirs.add((a, b))
        visited = [False] * n
        q = deque([0])
        visited[0] = True
        ans = 0
        while q:
            node = q.popleft()
            for neigh in adj[node]:
                if not visited[neigh]:
                    visited[neigh] = True
                    q.append(neigh)
                    if (node, neigh) in dirs:
                        ans += 1
        return ans
