class Solution:
    def findCircleNum(self, adj):
        n = len(adj)
        visited = [False] * n
        
        def explore(start):
            stack = [start]
            visited[start] = True
            while stack:
                curr = stack.pop()
                for neigh in range(n):
                    if adj[curr][neigh] and not visited[neigh]:
                        visited[neigh] = True
                        stack.append(neigh)
        
        groups = 0
        for i in range(n):
            if not visited[i]:
                explore(i)
                groups += 1
        return groups
