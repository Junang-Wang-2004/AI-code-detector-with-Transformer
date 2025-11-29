class Solution(object):
    def maxProfit(self, n, edges, score):
        predecessors = [[] for _ in range(n)]
        for u, v in edges:
            predecessors[v].append(u)
        N = 1 << n
        memo = [-1] * N
        memo[0] = 0
        counts = [0] * N
        for i in range(N):
            counts[i] = counts[i >> 1] + (i & 1)
        for current in range(N):
            if memo[current] == -1:
                continue
            length = counts[current] + 1
            for candidate in range(n):
                if current & (1 << candidate):
                    continue
                possible = True
                for prior in predecessors[candidate]:
                    if not (current & (1 << prior)):
                        possible = False
                        break
                if possible:
                    updated = current | (1 << candidate)
                    memo[updated] = max(memo[updated], memo[current] + length * score[candidate])
        return memo[N - 1]
