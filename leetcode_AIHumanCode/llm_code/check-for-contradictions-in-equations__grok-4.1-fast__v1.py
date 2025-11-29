from collections import defaultdict, deque

class Solution:
    def checkContradictions(self, equations, values):
        graph = defaultdict(list)
        nodes = set()
        for (x, y), r in zip(equations, values):
            if r == 0:
                continue
            graph[x].append((y, 1 / r))
            graph[y].append((x, r))
            nodes.add(x)
            nodes.add(y)
        ratios = {}
        TOL = 1e-9
        for root in list(nodes):
            if root in ratios:
                continue
            ratios[root] = 1.0
            queue = deque([root])
            while queue:
                curr = queue.popleft()
                for neigh, factor in graph[curr]:
                    anticipated = ratios[curr] * factor
                    if neigh in ratios:
                        diff = abs(ratios[neigh] - anticipated)
                        if diff > TOL * max(1.0, abs(ratios[neigh]), abs(anticipated)):
                            return True
                    else:
                        ratios[neigh] = anticipated
                        queue.append(neigh)
        return False
