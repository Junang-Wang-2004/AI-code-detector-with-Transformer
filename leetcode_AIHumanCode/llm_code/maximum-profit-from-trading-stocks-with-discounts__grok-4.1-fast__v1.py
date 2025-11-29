class Solution:
    def maxProfit(self, n, present, future, hierarchy, budget):
        graph = [[] for _ in range(n)]
        for p, c in hierarchy:
            graph[p - 1].append(c - 1)
        NEG = -10**18

        def compute(node):
            dp0 = [NEG] * (budget + 1)
            dp1 = [NEG] * (budget + 1)
            dp0[0] = dp1[0] = 0
            for nei in graph[node]:
                cdp0, cdp1 = compute(nei)
                ndp0 = [NEG] * (budget + 1)
                ndp1 = [NEG] * (budget + 1)
                for s in range(budget + 1):
                    if dp0[s] == NEG:
                        continue
                    for t in range(budget - s + 1):
                        if cdp0[t] == NEG:
                            continue
                        ndp0[s + t] = max(ndp0[s + t], dp0[s] + cdp0[t])
                for s in range(budget + 1):
                    if dp1[s] == NEG:
                        continue
                    for t in range(budget - s + 1):
                        if cdp1[t] == NEG:
                            continue
                        ndp1[s + t] = max(ndp1[s + t], dp1[s] + cdp1[t])
                dp0, dp1 = ndp0, ndp1
            out0 = [NEG] * (budget + 1)
            out1 = [NEG] * (budget + 1)
            for s in range(budget + 1):
                if dp0[s] != NEG:
                    out0[s] = max(out0[s], dp0[s])
                    out1[s] = max(out1[s], dp0[s])
            cfull = present[node]
            if cfull <= budget:
                gfull = future[node] - cfull
                for s in range(budget - cfull + 1):
                    if dp1[s] != NEG:
                        out0[s + cfull] = max(out0[s + cfull], dp1[s] + gfull)
            chalf = present[node] >> 1
            if chalf <= budget:
                ghalf = future[node] - chalf
                for s in range(budget - chalf + 1):
                    if dp1[s] != NEG:
                        out1[s + chalf] = max(out1[s + chalf], dp1[s] + ghalf)
            return out0, out1

        root0, _ = compute(0)
        return max(root0)
