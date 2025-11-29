import sys
sys.setrecursionlimit(10**5 + 10)

class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k):
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def compute(u, p):
            mod_sum = values[u] % k
            num_comps = 0
            for v in graph[u]:
                if v == p:
                    continue
                sub_comps, sub_mod = compute(v, u)
                num_comps += sub_comps
                if sub_mod == 0:
                    num_comps += 1
                else:
                    mod_sum = (mod_sum + sub_mod) % k
            return num_comps, mod_sum
        
        components, _ = compute(0, -1)
        return components + 1
