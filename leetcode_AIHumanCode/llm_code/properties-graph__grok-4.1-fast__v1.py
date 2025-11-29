class Solution:
    def numberOfComponents(self, properties, k):
        n = len(properties)
        prop_sets = [set(p) for p in properties]
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def unite(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[px] = py
        
        for i in range(n):
            for j in range(i + 1, n):
                if len(prop_sets[i] & prop_sets[j]) >= k:
                    unite(i, j)
        
        components = set(find(i) for i in range(n))
        return len(components)
