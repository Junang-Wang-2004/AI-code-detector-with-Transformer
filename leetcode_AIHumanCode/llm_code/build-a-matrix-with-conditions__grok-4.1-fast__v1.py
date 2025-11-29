class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        def compute_order(conds):
            graph = [[] for _ in range(k)]
            indegree = [0] * k
            for x, y in conds:
                ux = x - 1
                uy = y - 1
                graph[ux].append(uy)
                indegree[uy] += 1
            q = [i for i in range(k) if indegree[i] == 0]
            seq = []
            while q:
                node = q.pop(0)
                seq.append(node)
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        q.append(neigh)
            return seq

        rows = compute_order(rowConditions)
        if len(rows) != k:
            return []
        cols = compute_order(colConditions)
        if len(cols) != k:
            return []

        row_place = [0] * k
        col_place = [0] * k
        for pos, idx in enumerate(rows):
            row_place[idx] = pos
        for pos, idx in enumerate(cols):
            col_place[idx] = pos

        grid = [[0] * k for _ in range(k)]
        for val in range(1, k + 1):
            i = val - 1
            grid[row_place[i]][col_place[i]] = val
        return grid
