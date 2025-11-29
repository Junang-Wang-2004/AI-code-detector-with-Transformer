# Time:  O(n)
# Space: O(n)
# dfs, hash table
class Solution2(object):
    def findSubtreeSizes(self, parent, s):
        """
        """
        def dfs(u):
            lookup[ord(s[u])-ord('a')].append(u)
            for v in adj[u]:
                dfs(v)
                result[lookup[ord(s[v])-ord('a')][-1] if lookup[ord(s[v])-ord('a')] else u] += result[v]
            lookup[ord(s[u])-ord('a')].pop()
        
        adj = [[] for _ in range(len(parent))]
        for v, u in enumerate(parent):
            if u != -1:
                adj[u].append(v)
        lookup = [[] for _ in range(26)]
        result = [1]*len(parent)
        dfs(0)
        return result
