import heapq

class SegTree:
    def __init__(self, n):
        self.n = n
        self.inf = n + 10
        self.tree = [self.inf] * (4 * n)
        self._build(1, 0, n - 1)

    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = start
            return
        mid = (start + end) // 2
        self._build(2 * node, start, mid)
        self._build(2 * node + 1, mid + 1, end)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, idx, val):
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self._update(2 * node, start, mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return self.inf
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self._query(2 * node, start, mid, left, right)
        p2 = self._query(2 * node + 1, mid + 1, end, left, right)
        return min(p1, p2)

class Solution:
    def busiestServers(self, k, arrival, load):
        if k == 0:
            return []
        jobs = [0] * k
        tree = SegTree(k)
        ends = []
        for i in range(len(arrival)):
            t, duration = arrival[i], load[i]
            pos = i % k
            while ends and ends[0][0] <= t:
                _, server = heapq.heappop(ends)
                tree.update(server, server)
            server = tree.query(pos, k - 1)
            if server == tree.inf:
                server = tree.query(0, k - 1)
            if server == tree.inf:
                continue
            jobs[server] += 1
            tree.update(server, tree.inf)
            heapq.heappush(ends, (t + duration, server))
        max_jobs = max(jobs)
        return [j for j in range(k) if jobs[j] == max_jobs]
