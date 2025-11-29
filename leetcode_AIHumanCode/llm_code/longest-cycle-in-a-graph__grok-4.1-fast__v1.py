class Solution(object):
    def longestCycle(self, edges):
        n = len(edges)
        vis = [False] * n
        ans = -1
        for u in range(n):
            if vis[u]:
                continue
            path_pos = {}
            chain = []
            v = u
            while not vis[v] and v not in path_pos:
                path_pos[v] = len(chain)
                chain.append(v)
                v = edges[v]
            if v in path_pos:
                ans = max(ans, len(chain) - path_pos[v])
            for w in chain:
                vis[w] = True
        return ans
