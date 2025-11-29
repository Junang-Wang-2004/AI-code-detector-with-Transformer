# Time:  O(n)
# Space: O(h)
import collections


class Solution2(object):
    def countSubTrees(self, n, edges, labels):
        """
        """
        def dfs(labels, adj, node, parent, result):
            count = [0]*26
            for child in adj[node]:
                if child == parent:
                    continue
                new_count = dfs(labels, adj, child, node, result)
                for k in range(len(new_count)):
                    count[k] += new_count[k]
            count[ord(labels[node]) - ord('a')] += 1
            result[node] = count[ord(labels[node]) - ord('a')]
            return count
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = [0]*n
        dfs(labels, adj, 0, -1, result)
        return result
