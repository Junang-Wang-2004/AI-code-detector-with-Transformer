import collections


class Solution:
    def shortestPathLength(self, graph):
        num_nodes = len(graph)
        complete_mask = (1 << num_nodes) - 1
        distance = {}
        queue = collections.deque()
        for origin in range(num_nodes):
            bitmask = 1 << origin
            distance[(bitmask, origin)] = 0
            queue.append((bitmask, origin))
        while queue:
            bitmask, current = queue.popleft()
            steps = distance[(bitmask, current)]
            for adjacent in graph[current]:
                next_bitmask = bitmask | (1 << adjacent)
                pair = (next_bitmask, adjacent)
                if pair not in distance:
                    distance[pair] = steps + 1
                    queue.append(pair)
        min_length = float('inf')
        for final_pos in range(num_nodes):
            end_pair = (complete_mask, final_pos)
            if end_pair in distance:
                min_length = min(min_length, distance[end_pair])
        return min_length
