class Solution(object):
    def largestPathValue(self, colors, edges):
        n = len(colors)
        graph = [[] for _ in range(n)]
        for fr, to in edges:
            graph[fr].append(to)
        memo = [None] * n
        on_path = [False] * n
        cycle_exists = False
        best = 0
        def get_maxes(node):
            nonlocal cycle_exists, best
            if memo[node] is not None:
                return memo[node]
            if on_path[node]:
                cycle_exists = True
                return [0] * 26
            on_path[node] = True
            c_idx = ord(colors[node]) - ord('a')
            child_best = [0] * 26
            for child in graph[node]:
                sub_maxes = get_maxes(child)
                for j in range(26):
                    child_best[j] = max(child_best[j], sub_maxes[j])
            curr_maxes = [(1 if j == c_idx else 0) + child_best[j] for j in range(26)]
            on_path[node] = False
            memo[node] = curr_maxes
            best = max(best, max(curr_maxes))
            return curr_maxes
        for start in range(n):
            if memo[start] is None:
                get_maxes(start)
        return -1 if cycle_exists else best
