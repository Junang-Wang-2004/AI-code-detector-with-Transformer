import sys
from collections import deque
input = sys.stdin.readline

class C1:

    def __init__(self, a1=None, a2=None, a3=None, a4=None, a5=None, a6=float('inf')):
        self.V = a1
        self.E = a2
        self.lis = a3
        self.start = a4 if a4 else 0
        self.end = a5 if a5 else self.V - 1
        self.inf = a6
        self.close_minus = False

    def getlist(self, a1):
        self.lis = a1

    def def_start(self, a1):
        self.start = a1

    def def_end(self, a1):
        self.end = a1

    def def_inf(self, a1):
        self.inf = a1

    def def_vertice(self, a1):
        self.V = a1

    def def_edge(self, a1):
        self.E = a1

    def prepare(self):
        self.cost = [self.inf] * self.V
        self.cost[self.start] = 0

    def search(self):
        for v1 in range(self.V):
            v2 = False
            for v3, v4, v5 in self.lis:
                if self.cost[v4] > self.cost[v3] + v5:
                    self.cost[v4] = self.cost[v3] + v5
                    v2 = True
            if not v2:
                break
            if v1 == self.V - 1:
                self.close_minus = True
                return False
        return True

    def f11(self):
        self.prepare()
        self.search()

    def cost_all(self):
        return self.cost

def f11():
    v1, v2, v3 = map(int, input().split())
    v4 = [None] * v2
    v5 = [[] for v6 in range(v1)]
    v7 = [[] for v6 in range(v1)]
    for v8 in range(v2):
        v9, v10, v11 = map(int, input().split())
        v5[v9 - 1].append(v10 - 1)
        v7[v10 - 1].append(v9 - 1)
        v11 = v3 - v11
        v4[v8] = (v9 - 1, v10 - 1, v11)
    v12, v13 = ([True] * v1, [True] * v1)
    for v14, v15, v16 in zip([v12, v13], [v5, v7], [0, v1 - 1]):
        v17 = deque([v16])
        v14[v16] = False
        while v17:
            v18 = v17.pop()
            for v19 in v15[v18]:
                if v14[v19] == False:
                    continue
                v14[v19] = False
                v17.append(v19)
    v20 = []
    for v8 in range(v2):
        v9, v10, v11 = v4[v8]
        if v12[v9] or v12[v10] or v13[v9] or v13[v10]:
            continue
        v20.append((v9, v10, v11))
    v21 = C1(v=v1, e=v2, lis=v20)
    v21.main()
    if v21.close_minus:
        print(-1)
    else:
        print(max(0, -v21.cost[v1 - 1]))
if __name__ == '__main__':
    f11()
