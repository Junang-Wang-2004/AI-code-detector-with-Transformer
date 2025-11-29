class Solution(object):
    def maximumRequests(self, n, requests):
        self.best = 0
        deg = [0] * n

        def search(idx, num, deg):
            remain = len(requests) - idx
            if num + remain <= self.best:
                return
            if max(map(abs, deg)) > remain:
                return
            if idx == len(requests):
                if all(d == 0 for d in deg):
                    self.best = num
                return
            u, v = requests[idx]
            deg[u] -= 1
            deg[v] += 1
            search(idx + 1, num + 1, deg)
            deg[u] += 1
            deg[v] -= 1
            search(idx + 1, num, deg)

        search(0, 0, deg)
        return self.best
