from collections import deque

class Solution:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        adj = [[] for _ in range(n)]
        for a, b in richer:
            adj[a].append(b)
        indegree = [0] * n
        for i in range(n):
            for j in adj[i]:
                indegree[j] += 1
        q = deque(i for i in range(n) if indegree[i] == 0)
        ans = list(range(n))
        while q:
            u = q.popleft()
            for v in adj[u]:
                if quiet[ans[u]] < quiet[ans[v]]:
                    ans[v] = ans[u]
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return ans
