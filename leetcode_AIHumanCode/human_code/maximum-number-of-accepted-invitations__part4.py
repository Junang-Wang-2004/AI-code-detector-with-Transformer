# Time:  O(|V| * |E|) = O(min(m, n) * (m * n))
# Space: O(|E|) = O(m * n)
import collections


# Hungarian bipartite matching
class Solution3(object):
    def maximumInvitations(self, grid):
        """
        """
        def augment(adj, u, lookup, match):
            for v in adj[u]:
                if v in lookup:
                    continue
                lookup.add(v)
                if v not in match or augment(adj, match[v], lookup, match):
                    match[v] = u  # greedily match
                    return True
            return False
    
        def hungarian(adj):
            match = {}
            for i in adj.keys():
                augment(adj, i, set(), match)
            return len(match)
        
        adj = collections.defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    continue
                if len(grid) < len(grid[0]):
                    adj[i].append(j)
                else:
                    adj[j].append(i)
        return hungarian(adj)
