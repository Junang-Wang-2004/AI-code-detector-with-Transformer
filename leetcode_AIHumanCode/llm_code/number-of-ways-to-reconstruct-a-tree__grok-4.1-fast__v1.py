import collections

class Solution(object):
    def checkWays(self, pairs):
        graph = collections.defaultdict(set)
        for u, v in pairs:
            graph[u].add(v)
            graph[v].add(u)
        node_count = len(graph)
        if node_count == 0:
            return 1
        ordered_nodes = sorted(graph, key=lambda nd: len(graph[nd]), reverse=True)
        visited = set()
        root = ordered_nodes[0]
        visited.add(root)
        if len(graph[root]) != node_count - 1:
            return 0
        has_multiple = False
        for nd in ordered_nodes[1:]:
            visited.add(nd)
            prev_neighbors = [nbr for nbr in graph[nd] if nbr in visited]
            if not prev_neighbors:
                return 0
            prnt = min(prev_neighbors, key=lambda nbr: len(graph[nbr]))
            for nbr in graph[nd]:
                if nbr != prnt and nbr not in graph[prnt]:
                    return 0
            if len(graph[nd]) == len(graph[prnt]):
                has_multiple = True
        return 2 if has_multiple else 1
