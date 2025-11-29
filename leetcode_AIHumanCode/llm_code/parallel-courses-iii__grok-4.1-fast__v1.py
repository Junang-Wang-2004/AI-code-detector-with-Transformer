class Solution:
    def minimumTime(self, n, relations, time):
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in relations:
            graph[u - 1].append(v - 1)
            indegree[v - 1] += 1
        from collections import deque
        queue = deque(i for i in range(n) if indegree[i] == 0)
        result = [0] * n
        for i in range(n):
            if indegree[i] == 0:
                result[i] = time[i]
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                result[neighbor] = max(result[neighbor], result[node] + time[neighbor])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return max(result)
