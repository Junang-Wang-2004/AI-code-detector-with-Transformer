class Solution:
    def constructGridLayout(self, n, edges):
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        min_deg = min(map(len, graph))
        corners = [i for i in range(n) if len(graph[i]) == min_deg]
        start = corners[0]

        def get_dist(g, nn, origin):
            distance = [-1] * nn
            distance[origin] = 0
            pending = [origin]
            while pending:
                next_pending = []
                for vertex in pending:
                    for adj_node in g[vertex]:
                        if distance[adj_node] != -1:
                            continue
                        distance[adj_node] = distance[vertex] + 1
                        next_pending.append(adj_node)
                pending = next_pending
            return distance

        dist_start = get_dist(graph, n, start)
        closest_d = float('inf')
        second_corner = -1
        for cand in corners:
            if cand != start and dist_start[cand] < closest_d:
                closest_d = dist_start[cand]
                second_corner = cand
        width = dist_start[second_corner] + 1
        height = n // width
        dist_second = get_dist(graph, n, second_corner)
        layout = [[0] * width for _ in range(height)]
        delta = width - 1
        for node_id in range(n):
            da = dist_start[node_id]
            db = dist_second[node_id]
            rpos = (da + db - delta) // 2
            cpos = da - rpos
            layout[rpos][cpos] = node_id
        return layout
