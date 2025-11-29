# Time:  O(nlogr), r is sum(values)
# Space: O(n)
# dfs, trie, greedy
class Trie(object):
    def __init__(self, bit_length):
        self.__root = {}
        self.__bit_length = bit_length
        
    def insert(self, num):
        node = self.__root
        for i in reversed(range(self.__bit_length)):
            curr = (num>>i) & 1
            if curr not in node:
                node[curr] = {}
            node = node[curr]
                
    def query(self, num):
        if not self.__root: 
            return -1
        node, result = self.__root, 0
        for i in reversed(range(self.__bit_length)):
            curr = (num>>i) & 1
            if 1^curr in node:
                node = node[1^curr]
                result |= 1<<i
            else:
                node = node[curr]
        return result


class Solution2(object):
    def maxXor(self, n, edges, values):
        """
        """
        def dfs(u, p):
            lookup[u] = values[u]+sum(dfs(v, u) for v in adj[u] if v != p)
            return lookup[u]

        def dfs2(u, p):
            result = max(trie.query(lookup[u]), 0)
            for v in adj[u]:
                if v == p:
                    continue
                result = max(result, dfs2(v, u))
            trie.insert(lookup[u])
            return result
        
        adj = [[] for _ in range(len(values))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lookup = [0]*len(values)
        dfs(0, -1)
        trie = Trie(lookup[0].bit_length())
        return dfs2(0, -1)
