from collections import deque

class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        graph_red = [[] for _ in range(n)]
        graph_blue = [[] for _ in range(n)]
        for u, v in red_edges:
            graph_red[u].append(v)
        for u, v in blue_edges:
            graph_blue[u].append(v)
        LARGE = 2 * n + 5
        path_len = [[LARGE] * 2 for _ in range(n)]
        path_len[0][0] = path_len[0][1] = 0
        bfs_queue = deque([(0, 0), (0, 1)])
        while bfs_queue:
            node, edge_color = bfs_queue.popleft()
            next_edge_color = 1 - edge_color
            adj = graph_red[node] if edge_color == 0 else graph_blue[node]
            for next_node in adj:
                if path_len[next_node][edge_color] == LARGE:
                    path_len[next_node][edge_color] = path_len[node][next_edge_color] + 1
                    bfs_queue.append((next_node, next_edge_color))
        result = []
        for i in range(n):
            min_path = min(path_len[i])
            result.append(min_path if min_path < LARGE else -1)
        return result
