# Time:  O(n^2)
# Space: O(n)
import collections


# bfs
class Solution2(object):
    def maxAmount(self, initialCurrency, pairs1, rates1, pairs2, rates2):
        """
        """
        def find_adj(pairs, rates):
            adj = collections.defaultdict(list)
            for i in range(len(pairs)):
                adj[pairs[i][0]].append((pairs[i][1], rates[i]))
                adj[pairs[i][1]].append((pairs[i][0], 1/rates[i]))
            return adj

        def bfs(dist, adj):
            q = list(dist.keys())
            while q:
                new_q = []
                for u in q:
                    for v, w in adj[u]:
                        if not w*dist[u] > dist[v]:
                            continue
                        dist[v] = w*dist[u]
                        new_q.append(v)
                q = new_q
            return dist
    
        dist = collections.defaultdict(int)
        dist[initialCurrency] = 1.0
        adj1 = find_adj(pairs1, rates1)
        bfs(dist, adj1)  # Time: O(n)
        adj2 = find_adj(pairs2, rates2)
        bfs(dist, adj2)  # Time: O(n^2)
        return dist[initialCurrency]
