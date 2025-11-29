class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        adj = {}
        for u, v in edges:
            if u not in adj:
                adj[u] = []
            adj[u].append(v)
        visiting = set()
        finished = set()
        def validate(node):
            if node in finished:
                return True
            if node in visiting:
                return False
            visiting.add(node)
            neighbors = adj.get(node, [])
            if len(neighbors) == 0 and node != destination:
                visiting.remove(node)
                return False
            for next_node in neighbors:
                if not validate(next_node):
                    visiting.remove(node)
                    return False
            visiting.remove(node)
            finished.add(node)
            return True
        return validate(source)
