class Solution:
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n
        
        def check_component(start):
            if visited[start]:
                return False
            component_size = 0
            degree_total = 0
            stack = [start]
            visited[start] = True
            while stack:
                curr = stack.pop()
                component_size += 1
                degree_total += len(graph[curr])
                for neighbor in graph[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            return component_size * (component_size - 1) == degree_total
        
        return sum(check_component(i) for i in range(n) if not visited[i])
