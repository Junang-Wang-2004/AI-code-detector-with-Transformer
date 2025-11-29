class Solution(object):
    def putMarbles(self, weights, k):
        adj = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        adj.sort()
        num = k - 1
        return sum(adj[-num:]) - sum(adj[:num])
