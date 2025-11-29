import collections

class C1(object):

    def __init__(self, a1):
        self.n = a1
        self.tree = [0] * (a1 + 2)

    def update(self, a1, a2):
        while a1 <= self.n:
            self.tree[a1] += a2
            a1 += a1 & -a1

    def prefix_sum(self, a1):
        v1 = 0
        while a1 > 0:
            v1 += self.tree[a1]
            a1 -= a1 & -a1
        return v1

class C2(object):

    def minInteger(self, a1, a2):
        v1 = len(a1)
        v2 = C1(v1)
        for v3 in range(1, v1 + 1):
            v2.update(v3, 1)
        v4 = [collections.deque() for v5 in range(10)]
        for v3 in range(v1):
            v6 = int(a1[v3])
            v4[v6].append(v3 + 1)
        v7 = []
        for v5 in range(v1):
            for v6 in range(10):
                if v4[v6]:
                    v8 = v4[v6][0]
                    v9 = v2.prefix_sum(v8 - 1)
                    if v9 <= a2:
                        a2 -= v9
                        v2.update(v8, -1)
                        v4[v6].popleft()
                        v7.append(str(v6))
                        break
        return ''.join(v7)
