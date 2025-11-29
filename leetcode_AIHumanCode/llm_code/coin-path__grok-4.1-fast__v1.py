class Solution:
    def cheapestJump(self, A, B):
        if not A or A[-1] == -1:
            return []
        n = len(A)
        INF = float('inf')
        costs = [INF] * n
        parents = [-1] * n
        if A[0] != -1:
            costs[0] = A[0]
        for i in range(n):
            if costs[i] == INF or A[i] == -1:
                continue
            for j in range(i + 1, min(n, i + B + 1)):
                if A[j] == -1:
                    continue
                candidate = costs[i] + A[j]
                if candidate < costs[j]:
                    costs[j] = candidate
                    parents[j] = i
        if costs[n - 1] == INF:
            return []
        path = []
        curr = n - 1
        while curr != -1:
            path.append(curr + 1)
            curr = parents[curr]
        path.reverse()
        return path
