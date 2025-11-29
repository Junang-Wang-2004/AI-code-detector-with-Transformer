class Solution:
    def minScore(self, n, roads):
        neighbors = [[] for _ in range(n)]
        for x, y, score in roads:
            neighbors[x - 1].append(y - 1)
            neighbors[y - 1].append(x - 1)
        visited = [False] * n
        queue = [0]
        visited[0] = True
        while queue:
            next_queue = []
            for node in queue:
                for adj_node in neighbors[node]:
                    if not visited[adj_node]:
                        visited[adj_node] = True
                        next_queue.append(adj_node)
            queue = next_queue
        return min(score for x, y, score in roads if visited[x - 1] or visited[y - 1])
