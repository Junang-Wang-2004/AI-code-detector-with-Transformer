class Solution(object):
    def maximalPathQuality(self, values, edges, maxTime):
        n = len(values)
        graph = [[] for _ in range(n)]
        for a, b, c in edges:
            graph[a].append((b, c))
            graph[b].append((a, c))
        counts = [0] * n
        def traverse(node, time_avail, path_sum):
            counts[node] += 1
            updated_sum = path_sum + (values[node] if counts[node] == 1 else 0)
            current_max = updated_sum if node == 0 else 0
            for neighbor, cost in graph[node]:
                edge_id = (node, neighbor)
                if time_avail < cost or edge_id in used_edges:
                    continue
                used_edges.add(edge_id)
                current_max = max(current_max, traverse(neighbor, time_avail - cost, updated_sum))
                used_edges.remove(edge_id)
            counts[node] -= 1
            return current_max
        used_edges = set()
        return traverse(0, maxTime, 0)
