class Solution(object):
    def remainingMethods(self, n, k, invocations):
        graph = [[] for _ in range(n)]
        for src, dst in invocations:
            graph[src].append(dst)
        reachable = [False] * n
        reachable[k] = True
        queue = [k]
        while queue:
            next_queue = []
            for node in queue:
                for neighbor in graph[node]:
                    if not reachable[neighbor]:
                        reachable[neighbor] = True
                        next_queue.append(neighbor)
            queue = next_queue
        has_invalid_edge = any(not reachable[frm] and reachable[to] for frm, to in invocations)
        if has_invalid_edge:
            return list(range(n))
        return [idx for idx in range(n) if not reachable[idx]]
