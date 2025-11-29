import sys
input = sys.stdin.readline
from collections import deque

class C1:

    def __init__(self, a1, a2, a3=0):
        self.v = a1
        self.Edges = a2
        self.maxLog = 18
        self.Parent = [[-1] * a1 for v1 in range(self.maxLog + 1)]
        self.Depth = [0] * a1
        self.__bfs(a3)
        for v2 in range(self.maxLog):
            for v3 in range(a1):
                if self.Parent[v2][v3] != -1:
                    self.Parent[v2 + 1][v3] = self.Parent[v2][self.Parent[v2][v3]]

    def __bfs(self, a1):
        v1 = [False] * self.v
        v1[a1] = True
        v2 = deque([a1])
        while v2:
            v3 = v2.pop()
            for v4 in self.Edges[v3]:
                if v1[v4]:
                    continue
                self.Parent[0][v4] = v3
                self.Depth[v4] = self.Depth[v3] + 1
                v1[v4] = True
                v2.append(v4)

    def lca(self, a1, a2):
        if self.Depth[a1] > self.Depth[a2]:
            a1, a2 = (a2, a1)
        for v3 in range(self.maxLog):
            if self.Depth[a2] - self.Depth[a1] & 1 << v3:
                a2 = self.Parent[v3][a2]
        if a1 == a2:
            return a2
        for v3 in reversed(range(self.maxLog - 1)):
            if self.Parent[v3][a1] != self.Parent[v3][a2]:
                a1 = self.Parent[v3][a1]
                a2 = self.Parent[v3][a2]
        return self.Parent[0][a1]

    def dist(self, a1, a2):
        v1 = self.lca(a1, a2)
        return self.Depth[a1] + self.Depth[a2] - 2 * self.Depth[v1]

def f4():
    v1, v2, v3 = map(int, input().split())
    v2 -= 1
    v3 -= 1
    v4 = [[] for v5 in range(v1)]
    for v5 in range(v1 - 1):
        v6, v7 = map(lambda i: int(i) - 1, input().split())
        v4[v6].append(v7)
        v4[v7].append(v6)
    v8 = []
    for v9 in range(v1):
        if len(v4[v9]) == 1:
            v8.append(v9)
    v10 = C1(v1, v4)
    v11 = 0
    for v12 in v8:
        v13 = v10.dist(v2, v12)
        v14 = v10.dist(v3, v12)
        if v13 >= v14:
            continue
        v11 = max(v11, v13 + (v14 - v13) // 2)
    print(v11)
if __name__ == '__main__':
    f4()
