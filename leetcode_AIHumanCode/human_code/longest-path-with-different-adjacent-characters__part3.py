# Time:  O(n)
# Space: O(h)
# tree, dfs
class Solution3(object):
    def longestPath(self, parent, s):
        """
        """
        def dfs(s, adj, u, result):
            top2 = [0]*2
            for v in adj[u]:
                l = dfs(s, adj, v, result)
                if s[v] == s[u]:
                    continue
                if l > top2[0]:
                    top2[0], top2[1] = l, top2[0]
                elif l > top2[1]:
                    top2[1] = l
            result[0] = max(result[0], top2[0]+top2[1]+1)
            return top2[0]+1
    
        
        adj = [[] for _ in range(len(s))]
        for i in range(1, len(parent)):
            adj[parent[i]].append(i)
        result = [0]
        dfs(s, adj, 0, result)
        return result[0]
    
