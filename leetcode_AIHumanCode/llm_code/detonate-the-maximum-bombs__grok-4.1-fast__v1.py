class Solution:
    def maximumDetonation(self, bombs):
        n = len(bombs)
        graph = [[] for _ in range(n)]
        for u in range(n):
            ux, uy, ur = bombs[u]
            for v in range(n):
                if u == v:
                    continue
                vx, vy = bombs[v][0], bombs[v][1]
                dx, dy = ux - vx, uy - vy
                if dx * dx + dy * dy <= ur * ur:
                    graph[u].append(v)
        
        def dfs(node, visited):
            visited[node] = True
            for adj_node in graph[node]:
                if not visited[adj_node]:
                    dfs(adj_node, visited)
        
        max_size = 0
        for start in range(n):
            vis = [False] * n
            dfs(start, vis)
            curr_size = sum(vis)
            if curr_size > max_size:
                max_size = curr_size
            if max_size == n:
                return n
        return max_size
