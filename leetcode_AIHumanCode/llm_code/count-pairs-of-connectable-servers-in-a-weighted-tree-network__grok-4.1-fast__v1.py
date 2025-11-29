class Solution:
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        n = len(edges) + 1
        adj_list = [[] for _ in range(n)]
        for src, dst, wt in edges:
            adj_list[src].append((dst, wt))
            adj_list[dst].append((src, wt))
        output = [0] * n
        def subtree_goods(rt, prv, dmod):
            goods = int(dmod % signalSpeed == 0)
            for nxt, ew in adj_list[rt]:
                if nxt != prv:
                    goods += subtree_goods(nxt, rt, dmod + ew)
            return goods
        for pivot in range(n):
            sub_counts = [subtree_goods(nei, pivot, w) for nei, w in adj_list[pivot]]
            output[pivot] = sum(sub_counts[i] * sum(sub_counts[:i]) for i in range(len(sub_counts)))
        return output
