class Solution:
    def getAncestors(self, n, edges):
        incoming = [[] for _ in range(n)]
        for a, b in edges:
            incoming[b].append(a)
        cache = [None] * n
        
        def compute(node):
            if cache[node] is not None:
                return cache[node]
            s = set()
            for prev in incoming[node]:
                s.add(prev)
                s |= compute(prev)
            cache[node] = s
            return s
        
        output = []
        for i in range(n):
            ancestors = compute(i)
            output.append(sorted(ancestors))
        return output
