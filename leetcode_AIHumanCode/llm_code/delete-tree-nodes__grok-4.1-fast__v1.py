class Solution:
    def deleteTreeNodes(self, n, parent, vals):
        graph = [[] for _ in range(n)]
        for i in range(1, n):
            graph[parent[i]].append(i)
        
        def traverse(u):
            subsum = vals[u]
            sz = 1
            for v in graph[u]:
                tsum, tsz = traverse(v)
                subsum += tsum
                if tsum != 0:
                    sz += tsz
            if subsum == 0:
                return 0, 0
            return subsum, sz
        
        _, remaining = traverse(0)
        return remaining
