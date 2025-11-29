class Solution:
    def countVisitedNodes(self, edges):
        n = len(edges)
        result = [0] * n
        processed = [False] * n
        for start in range(n):
            if processed[start]:
                continue
            path = []
            on_path = set()
            node = start
            while True:
                if processed[node]:
                    value = result[node]
                    for k in range(len(path) - 1, -1, -1):
                        value += 1
                        result[path[k]] = value
                    break
                if node in on_path:
                    cyc_start = path.index(node)
                    cyc_len = len(path) - cyc_start
                    for k in range(cyc_start, len(path)):
                        result[path[k]] = cyc_len
                    value = cyc_len
                    for k in range(cyc_start - 1, -1, -1):
                        value += 1
                        result[path[k]] = value
                    break
                on_path.add(node)
                path.append(node)
                node = edges[node]
            for p in path:
                processed[p] = True
        return result
