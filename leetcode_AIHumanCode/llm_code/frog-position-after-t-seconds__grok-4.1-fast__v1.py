from collections import defaultdict, deque

class Solution:
    def frogPosition(self, n, edges, t, target):
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        if target not in graph:
            return 0.0
        
        parents = {}
        depths = {}
        queue = deque([1])
        parents[1] = None
        depths[1] = 0
        
        while queue:
            curr = queue.popleft()
            if curr == target:
                break
            for neigh in graph[curr]:
                if neigh != parents.get(curr):
                    parents[neigh] = curr
                    depths[neigh] = depths[curr] + 1
                    queue.append(neigh)
        
        if target not in depths:
            return 0.0
        
        dist = depths[target]
        if dist > t:
            return 0.0
        
        out_degree = len(graph[target]) - (0 if parents.get(target) is None else 1)
        if dist < t and out_degree > 0:
            return 0.0
        
        probability = 1.0
        node = target
        while node != 1:
            prev = parents[node]
            branches = len(graph[prev]) - (0 if prev == 1 else 1)
            probability /= branches
            node = prev
        
        return probability
