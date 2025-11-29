class C1:

    def __init__(self, a1, a2):
        self.edge = a2
        self.n = a1
        self.dist = [float('inf')] * self.n
        self.prev = [None] * self.n

    def fit(self):
        self.dist[0] = 0
        for v1 in range(self.n - 1):
            for v2, v3, v4 in self.edge:
                v5 = self.dist[v2] + v4
                if self.dist[v3] > v5:
                    self.dist[v3] = v5
                    self.prev[v3] = v2
v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v2):
    v6, v7, v8 = map(int, input().split())
    v4.append((v6 - 1, v7 - 1, v3 - v8))
v9 = C1(v1, v4)
v9.fit()
print(-min(0, v9.dist[-1]))
