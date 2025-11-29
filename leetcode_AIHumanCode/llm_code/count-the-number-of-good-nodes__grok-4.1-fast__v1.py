class Solution:
    def countGoodNodes(self, edges):
        n = len(edges)
        graph = [[] for _ in range(n + 1)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        self.count = 0
        
        def traverse(curr, parent):
            child_sizes = []
            for neigh in graph[curr]:
                if neigh != parent:
                    child_sizes.append(traverse(neigh, curr))
            if len(child_sizes) == 0 or len(child_sizes) == 1 or all(sz == child_sizes[0] for sz in child_sizes):
                self.count += 1
            return 1 + sum(child_sizes)
        
        traverse(0, -1)
        return self.count
