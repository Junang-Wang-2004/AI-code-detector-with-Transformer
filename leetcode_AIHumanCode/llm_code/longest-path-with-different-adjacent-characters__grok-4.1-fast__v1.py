from collections import deque

class Solution:
    def longestPath(self, parent, s):
        n = len(s)
        rev_adj = [[] for _ in range(n)]
        indegree = [0] * n
        for i in range(1, n):
            p = parent[i]
            rev_adj[i].append(p)
            indegree[p] += 1
        longest = [[0, 0] for _ in range(n)]
        q = deque((i, 1) for i in range(n) if indegree[i] == 0)
        res = 1
        while q:
            nxt_q = deque()
            for u, d in q:
                for v in rev_adj[u]:
                    if s[v] != s[u]:
                        if d > longest[v][0]:
                            longest[v][1] = longest[v][0]
                            longest[v][0] = d
                        elif d > longest[v][1]:
                            longest[v][1] = d
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        nxt_d = longest[v][0] + 1
                        nxt_q.append((v, nxt_d))
                        res = max(res, longest[v][0] + longest[v][1] + 1)
            q = nxt_q
        return res
