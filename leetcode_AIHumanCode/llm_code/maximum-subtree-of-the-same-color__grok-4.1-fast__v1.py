class Solution:
    def maximumSubtreeSize(self, edges, colors):
        n = len(colors)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        max_size = [0]
        def dfs(curr, par):
            sz = 1
            valid = True
            for nxt in graph[curr]:
                if nxt == par:
                    continue
                sub = dfs(nxt, curr)
                if sub != -1 and colors[nxt] == colors[curr]:
                    sz += sub
                else:
                    valid = False
            if not valid:
                sz = -1
            max_size[0] = max(max_size[0], sz)
            return sz
        dfs(0, -1)
        return max_size[0]
