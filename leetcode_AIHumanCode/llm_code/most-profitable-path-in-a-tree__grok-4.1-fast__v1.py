class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        bob_dist_down = [float('inf')] * n

        def compute_bob_time(u, p):
            if u == bob:
                bob_dist_down[u] = 0
                return 0
            mind = float('inf')
            for v in adj[u]:
                if v == p:
                    continue
                cd = compute_bob_time(v, u)
                mind = min(mind, cd + 1)
            bob_dist_down[u] = mind
            return mind

        compute_bob_time(0, -1)

        def compute_profit(u, p, alice_t):
            bh = bob_dist_down[u]
            prof = amount[u]
            if alice_t == bh:
                prof //= 2
            elif alice_t > bh:
                prof = 0
            ch_max = 0
            for v in adj[u]:
                if v == p:
                    continue
                ch_max = max(ch_max, compute_profit(v, u, alice_t + 1))
            return prof + ch_max

        return compute_profit(0, -1, 0)
