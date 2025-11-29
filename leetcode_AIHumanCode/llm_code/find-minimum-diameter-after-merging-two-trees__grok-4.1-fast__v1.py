class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        def compute_diameter(tree):
            node_count = len(tree) + 1
            neighbors = [[] for _ in range(node_count)]
            for a, b in tree:
                neighbors[a].append(b)
                neighbors[b].append(a)
            
            def level_bfs(origin):
                seen = [False] * node_count
                seen[origin] = True
                queue = [origin]
                extremum = origin
                depth = 0
                while queue:
                    next_queue = []
                    for current in queue:
                        for adjacent in neighbors[current]:
                            if not seen[adjacent]:
                                seen[adjacent] = True
                                next_queue.append(adjacent)
                    if next_queue:
                        extremum = next_queue[-1]
                        queue = next_queue
                        depth += 1
                    else:
                        break
                return extremum, depth
            
            endpoint1, _ = level_bfs(0)
            _, length = level_bfs(endpoint1)
            return length
        
        len1 = compute_diameter(edges1)
        len2 = compute_diameter(edges2)
        mid1 = (len1 + 1) // 2
        mid2 = (len2 + 1) // 2
        return max(mid1 + mid2 + 1, len1, len2)
