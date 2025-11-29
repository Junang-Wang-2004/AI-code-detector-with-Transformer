class Solution:
    def placedCoins(self, edges, costs):
        n = len(costs)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res = [0] * n
        def dfs(curr, prev):
            my_val = costs[curr]
            best_smalls = [my_val]
            best_larges = [my_val]
            total_nodes = 1
            for neigh in graph[curr]:
                if neigh == prev:
                    continue
                ch_smalls, ch_larges, ch_nodes = dfs(neigh, curr)
                total_nodes += ch_nodes
                merged_smalls = sorted(best_smalls + ch_smalls)[:2]
                best_smalls = merged_smalls
                merged_larges = sorted(best_larges + ch_larges, reverse=True)[:3]
                best_larges = merged_larges
            if total_nodes < 3:
                res[curr] = 1
            else:
                p1 = best_smalls[0] * best_smalls[1] * best_larges[0]
                p2 = best_larges[0] * best_larges[1] * best_larges[2]
                res[curr] = max(p1, p2, 0)
            return best_smalls, best_larges, total_nodes
        dfs(0, -1)
        return res
