# Time:  O(n)
# Space: O(h)
# dfs
class Solution2(object):
    def maximumSubtreeSize(self, edges, colors):
        """
        """
        def dfs(u, p):
            cnt = 1
            for v in adj[u]:
                if v == p:
                    continue
                c = dfs(v, u)
                if cnt == -1:
                    continue
                if c == -1 or colors[v] != colors[u]:
                    cnt = -1
                    continue
                cnt += c
            result[0] = max(result[0], cnt)
            return cnt

        adj = [[] for _ in range(len(colors))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = [0]
        dfs(0, -1)
        return result[0]
