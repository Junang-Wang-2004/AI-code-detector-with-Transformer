# Time:  O(n^3 + q)
# Space: O(n^2)
import collections
import itertools


# variant of floyd–warshall algorithm solution
class Solution3(object):
    def calcEquation(self, equations, values, queries):
        """
        """
        adj = collections.defaultdict(dict)
        for (a, b), k in zip(equations, values):
            adj[a][a] = adj[b][b] = 1.0
            adj[a][b] = k
            adj[b][a] = 1.0/k
        for k in adj:
            for i in adj[k]:
                for j in adj[k]:
                    adj[i][j] = adj[i][k]*adj[k][j]
        return [adj[a].get(b, -1.0) for a, b in queries]

    
