class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        root = node
        while self.parent[root] != root:
            root = self.parent[root]
        cur = node
        while cur != root:
            next_node = self.parent[cur]
            self.parent[cur] = root
            cur = next_node
        return root

    def merge(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1


class Solution:
    def areConnected(self, n, threshold, queries):
        components = DSU(n)
        for divisor in range(threshold + 1, n + 1):
            candidate = divisor * 2
            while candidate <= n:
                components.merge(divisor - 1, candidate - 1)
                candidate += divisor
        output = []
        for edge in queries:
            x, y = edge
            output.append(components.find(x - 1) == components.find(y - 1))
        return output
