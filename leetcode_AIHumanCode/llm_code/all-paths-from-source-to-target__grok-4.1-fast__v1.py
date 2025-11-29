class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        answer = []
        stk = [(0, [0])]
        while stk:
            u, trail = stk.pop()
            if u == n - 1:
                answer.append(trail)
                continue
            for v in graph[u]:
                stk.append((v, trail + [v]))
        return answer
