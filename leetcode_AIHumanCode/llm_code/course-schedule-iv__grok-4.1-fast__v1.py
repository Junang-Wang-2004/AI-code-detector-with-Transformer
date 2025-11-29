class Solution:
    def checkIfPrerequisite(self, n, prerequisites, queries):
        graph = [[] for _ in range(n)]
        for u, v in prerequisites:
            graph[u].append(v)
        reachable_from = [None] * n
        for start in range(n):
            visited = set([start])
            queue = [start]
            idx = 0
            while idx < len(queue):
                curr = queue[idx]
                idx += 1
                for neigh in graph[curr]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)
            reachable_from[start] = visited
        result = []
        for a, b in queries:
            result.append(b in reachable_from[a])
        return result
