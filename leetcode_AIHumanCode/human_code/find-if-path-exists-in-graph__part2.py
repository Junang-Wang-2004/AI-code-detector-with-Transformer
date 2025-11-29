# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)
# bfs solution
class Solution2(object):
    def validPath(self, n, edges, start, end):
        """
        """
        def bfs(adj, start, target):
            q = [start]
            lookup = set(q)
            steps = 0
            while q:
                new_q = []
                for pos in q:
                    if pos == target:
                        return steps
                    for nei in adj[pos]:
                        if nei in lookup:
                            continue
                        lookup.add(nei)
                        new_q.append(nei)
                q = new_q
                steps += 1
            return -1  

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return bfs(adj, start, end) >= 0


