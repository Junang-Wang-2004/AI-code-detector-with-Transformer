class Solution:
    def waysToBuildRooms(self, prevRoom):
        MOD = 10**9 + 7
        n = len(prevRoom)
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[prevRoom[i]].append(i)
        
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [0] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        
        def comb(total, pick):
            if pick < 0 or pick > total:
                return 0
            return fact[total] * inv_fact[pick] % MOD * inv_fact[total - pick] % MOD
        
        def traverse(node):
            subtree_ways = 1
            cum_size = 0
            total_size = 1
            for neigh in tree[node]:
                neigh_ways, neigh_size = traverse(neigh)
                subtree_ways = subtree_ways * neigh_ways % MOD
                interleave = comb(cum_size + neigh_size, neigh_size)
                subtree_ways = subtree_ways * interleave % MOD
                cum_size += neigh_size
                total_size += neigh_size
            return subtree_ways, total_size
        
        return traverse(0)[0]
