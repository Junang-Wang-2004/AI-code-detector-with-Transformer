from collections import defaultdict

class Solution:
    def isPrintable(self, targetGrid):
        if not targetGrid or not targetGrid[0]:
            return True
        rows, cols = len(targetGrid), len(targetGrid[0])
        bounds = {}
        for i in range(rows):
            for j in range(cols):
                clr = targetGrid[i][j]
                if clr not in bounds:
                    bounds[clr] = [i, j, i, j]
                else:
                    b = bounds[clr]
                    b[0] = min(b[0], i)
                    b[1] = min(b[1], j)
                    b[2] = max(b[2], i)
                    b[3] = max(b[3], j)
        graph = defaultdict(set)
        for clr, (r_min, c_min, r_max, c_max) in bounds.items():
            for r in range(r_min, r_max + 1):
                for c in range(c_min, c_max + 1):
                    other = targetGrid[r][c]
                    if other != clr:
                        graph[clr].add(other)
        state = {}
        def detect_cycle(node):
            if node in state:
                return state[node] == 1
            state[node] = 1
            for neighbor in graph[node]:
                if detect_cycle(neighbor):
                    return True
            state[node] = 2
            return False
        for clr in bounds:
            if clr not in state:
                if detect_cycle(clr):
                    return False
        return True
