class Finder:
    def __init__(self, nn):
        self.par = list(range(nn))
        self.rnk = [0] * nn
        self.mx = list(range(nn))

    def root(self, i):
        if self.par[i] != i:
            self.par[i] = self.root(self.par[i])
        return self.par[i]

    def merge(self, i, j):
        pi = self.root(i)
        pj = self.root(j)
        if pi == pj:
            return
        if self.rnk[pi] < self.rnk[pj]:
            self.par[pi] = pj
            self.mx[pj] = max(self.mx[pi], self.mx[pj])
        else:
            self.par[pj] = pi
            self.mx[pi] = max(self.mx[pj], self.mx[pi])
            if self.rnk[pi] == self.rnk[pj]:
                self.rnk[pi] += 1

    def max_in(self, i):
        return self.mx[self.root(i)]


class Solution:
    def minReverseOperations(self, n, p, banned, k):
        is_banned = [False] * n
        for idx in banned:
            is_banned[idx] = True
        ans = [-1] * n
        ans[p] = 0
        finder = Finder(n + 2)
        finder.merge(p, p + 2)
        queue = [p]
        depth = 1
        while queue:
            next_queue = []
            for curr in queue:
                smin = max(0, curr - k + 1)
                smax = min(curr, n - k)
                lbound = 2 * smin + k - 1 - curr
                rbound = 2 * smax + k - 1 - curr
                idx = finder.max_in(lbound)
                while idx <= rbound:
                    if not is_banned[idx]:
                        ans[idx] = depth
                        next_queue.append(idx)
                    finder.merge(idx, idx + 2)
                    idx = finder.max_in(idx)
            queue = next_queue
            depth += 1
        return ans
