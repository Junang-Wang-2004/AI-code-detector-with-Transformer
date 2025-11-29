import collections

INF = float('inf')

class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        n = len(source)
        len_to_id = collections.defaultdict(dict)
        all_strs = collections.defaultdict(set)
        possible_lens = set()
        m = len(original)
        for i in range(m):
            l = len(original[i])
            possible_lens.add(l)
            all_strs[l].add(original[i])
            all_strs[l].add(changed[i])
        dists = {}
        for l, strs_set in all_strs.items():
            strs_list = sorted(strs_set)
            num_nodes = len(strs_list)
            id_map = {s: idx for idx, s in enumerate(strs_list)}
            len_to_id[l] = id_map
            graph = [[INF] * num_nodes for _ in range(num_nodes)]
            for j in range(num_nodes):
                graph[j][j] = 0
            dists[l] = graph
        for i in range(m):
            l = len(original[i])
            u = len_to_id[l][original[i]]
            v = len_to_id[l][changed[i]]
            dists[l][u][v] = min(dists[l][u][v], cost[i])
        def floyd_warshall(g):
            sz = len(g)
            for k in range(sz):
                for x in range(sz):
                    for y in range(sz):
                        g[x][y] = min(g[x][y], g[x][k] + g[k][y])
        for l in dists:
            floyd_warshall(dists[l])
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == INF:
                continue
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            for l in possible_lens:
                if i + l > n:
                    continue
                s_sub = source[i:i + l]
                t_sub = target[i:i + l]
                if s_sub in len_to_id[l] and t_sub in len_to_id[l]:
                    u = len_to_id[l][s_sub]
                    v = len_to_id[l][t_sub]
                    add = dists[l][u][v]
                    if add < INF:
                        dp[i + l] = min(dp[i + l], dp[i] + add)
        return dp[n] if dp[n] < INF else -1
