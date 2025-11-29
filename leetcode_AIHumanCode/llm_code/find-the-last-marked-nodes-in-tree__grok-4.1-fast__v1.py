class Solution:
    def lastMarkedNodes(self, edges):
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        farthest = [[(0, i), (0, i)] for i in range(n)]
        def first_pass(curr, prev):
            for neigh in adj[curr]:
                if neigh == prev:
                    continue
                first_pass(neigh, curr)
                cand_depth, cand_node = farthest[neigh][0]
                cand = (cand_depth + 1, cand_node)
                if cand > farthest[curr][0]:
                    farthest[curr][1] = farthest[curr][0]
                    farthest[curr][0] = cand
                elif cand > farthest[curr][1]:
                    farthest[curr][1] = cand
        first_pass(0, -1)
        answer = [0] * n
        def second_pass(curr, prev, incoming):
            best_down, _ = farthest[curr][0]
            best_in, _ = incoming
            answer[curr] = farthest[curr][0][1] if best_down >= best_in else incoming[1]
            for neigh in adj[curr]:
                if neigh == prev:
                    continue
                excl_idx = 1 if farthest[curr][0][1] == farthest[neigh][0][1] else 0
                excl_down = farthest[curr][excl_idx]
                max_out = excl_down if excl_down > incoming else incoming
                next_incoming = (max_out[0] + 1, max_out[1])
                second_pass(neigh, curr, next_incoming)
        second_pass(0, -1, (0, -1))
        return answer
