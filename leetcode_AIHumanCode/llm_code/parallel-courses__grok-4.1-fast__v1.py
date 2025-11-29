from collections import deque, defaultdict

class Solution:
    def minimumSemesters(self, n, relations):
        graph = defaultdict(list)
        indegree = [0] * n
        for pre, post in relations:
            graph[pre - 1].append(post - 1)
            indegree[post - 1] += 1
        q = deque(i for i in range(n) if indegree[i] == 0)
        sem = 0
        remaining = n
        while q:
            sem += 1
            level_size = len(q)
            for _ in range(level_size):
                u = q.popleft()
                remaining -= 1
                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
        return sem if remaining == 0 else -1
