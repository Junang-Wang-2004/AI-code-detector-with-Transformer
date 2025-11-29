class Solution(object):
    def maximumScore(self, scores, edges):
        n = len(scores)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        tops = []
        for i in range(n):
            top_neighbors = sorted(adj[i], key=lambda x: scores[x], reverse=True)[:3]
            tops.append(top_neighbors)
        ans = -1
        for a, b in edges:
            opts_a = [c for c in tops[a] if c != b]
            opts_b = [d for d in tops[b] if d != a]
            for c in opts_a:
                for d in opts_b:
                    if c != d:
                        ans = max(ans, scores[a] + scores[b] + scores[c] + scores[d])
        return ans
