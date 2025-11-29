class Solution:
    def reachableNodes(self, n, edges, restricted):
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        marked = [False] * n
        for nd in restricted:
            marked[nd] = True
        counter = [0]
        def explore(here):
            marked[here] = True
            counter[0] += 1
            for there in graph[here]:
                if not marked[there]:
                    explore(there)
        marked[0] = True
        explore(0)
        return counter[0]
