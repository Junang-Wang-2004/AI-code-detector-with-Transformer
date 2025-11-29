class Solution:
    def countPairs(self, n, edges):
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n
        sizes = []

        def component_size(start):
            stk = [start]
            visited[start] = True
            cnt = 1
            while stk:
                node = stk.pop()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        cnt += 1
                        stk.append(neighbor)
            return cnt

        for i in range(n):
            if not visited[i]:
                sizes.append(component_size(i))

        res = 0
        for s in sizes:
            res += s * (n - s)
        return res // 2
