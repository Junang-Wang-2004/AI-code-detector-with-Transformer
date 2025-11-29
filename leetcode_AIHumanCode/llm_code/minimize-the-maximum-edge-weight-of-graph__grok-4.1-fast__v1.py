class Solution:
    def minMaxWeight(self, n, edges, threshold):
        if n == 1:
            return 0
        graph = [{} for _ in range(n)]
        weights = set()
        for dest, src, wt in edges:
            if dest not in graph[src] or wt < graph[src][dest]:
                graph[src][dest] = wt
            weights.add(wt)
        if not weights:
            return -1
        sorted_weights = sorted(weights)
        def reachable(max_wt):
            visited = [False] * n
            visited[0] = True
            stack = [0]
            while stack:
                curr = stack.pop()
                for next_node, ewt in graph[curr].items():
                    if ewt <= max_wt and not visited[next_node]:
                        visited[next_node] = True
                        stack.append(next_node)
            return all(visited)
        l, r = 0, len(sorted_weights) - 1
        while l <= r:
            m = l + (r - l) // 2
            if reachable(sorted_weights[m]):
                r = m - 1
            else:
                l = m + 1
        return sorted_weights[l] if l < len(sorted_weights) else -1
