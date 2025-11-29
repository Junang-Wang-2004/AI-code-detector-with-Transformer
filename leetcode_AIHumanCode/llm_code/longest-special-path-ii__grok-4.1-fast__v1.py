class Solution:
    def longestSpecialPath(self, edges, nums):
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        lookup = {}
        prefix = [0]
        best = [float('inf'), float('inf')]
        def dfs(node, par, depth, max_one, max_two):
            col = nums[node] - 1
            prv = lookup.get(col, -1)
            lookup[col] = depth
            c1, c2 = max_one, max_two
            if c1 < c2:
                c1, c2 = c2, c1
            p = prv
            if p > c1:
                nm1, nm2 = p, c1
            elif p > c2:
                nm1, nm2 = c1, p
            else:
                nm1, nm2 = c1, c2
            ancestor = nm2
            path_w = prefix[depth] - prefix[ancestor + 1]
            path_h = depth - ancestor
            neg = -path_w
            if neg < best[0] or (neg == best[0] and path_h < best[1]):
                best[0] = neg
                best[1] = path_h
            for nxt, leng in adj[node]:
                if nxt == par: continue
                prefix.append(prefix[-1] + leng)
                dfs(nxt, node, depth + 1, nm1, nm2)
                prefix.pop()
            lookup[col] = prv
        dfs(0, -1, 0, -1, -1)
        return [-best[0], best[1]]
