class Solution:
    def maximizeSumOfWeights(self, edges, k):
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def explore(curr, prev):
            base_sum = 0
            benefits = []
            for next_node, edge_wt in graph[curr]:
                if next_node == prev:
                    continue
                max_with_cap, max_less_cap = explore(next_node, curr)
                base_sum += max_with_cap
                benefit = max(max_less_cap + edge_wt - max_with_cap, 0)
                benefits.append(benefit)
            benefits.sort(reverse=True)
            take_full = min(k, len(benefits))
            take_less = max(0, min(k - 1, len(benefits)))
            res_full = base_sum + sum(benefits[:take_full])
            res_less = base_sum + sum(benefits[:take_less])
            return res_full, res_less
        
        return explore(0, -1)[0]
