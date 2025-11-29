class C1(object):

    def maxJumps(self, a1, a2):
        """
        """
        v1, v2 = ([[] for v3 in range(len(a1))], [])
        for v4 in range(len(a1)):
            while v2 and a1[v2[-1]] < a1[v4]:
                if v4 - v2[-1] <= a2:
                    if v1[v4] and a1[v1[v4][-1]] != a1[v2[-1]]:
                        v1[v4] = []
                    v1[v4].append(v2[-1])
                v2.pop()
            v2.append(v4)
        v5, v2 = ([[] for v3 in range(len(a1))], [])
        for v4 in reversed(range(len(a1))):
            while v2 and a1[v2[-1]] < a1[v4]:
                if v2[-1] - v4 <= a2:
                    if v5[v4] and a1[v5[v4][-1]] != a1[v2[-1]]:
                        v5[v4] = []
                    v5[v4].append(v2[-1])
                v2.pop()
            v2.append(v4)
        v6 = [0] * len(a1)
        for v7, v4 in sorted(([v7, v4] for v4, v7 in enumerate(a1))):
            v6[v4] = 1
            for v8 in itertools.chain(v1[v4], v5[v4]):
                v6[v4] = max(v6[v4], v6[v8] + 1)
        return max(v6)

class C2(object):

    def __init__(self, a1, a2=lambda x, y: [y] * (2 * x), a3=max, a4=lambda x, y: y, a5=0):
        self.N = a1
        self.H = (a1 - 1).bit_length()
        self.query_fn = a3
        self.update_fn = a4
        self.default_val = a5
        self.tree = a2(a1, a5)
        self.lazy = [None] * a1

    def __apply(self, a1, a2):
        self.tree[a1] = self.update_fn(self.tree[a1], a2)
        if a1 < self.N:
            self.lazy[a1] = self.update_fn(self.lazy[a1], a2)

    def update(self, a1, a2, a3):

        def pull(a1):
            while a1 > 1:
                a1 //= 2
                self.tree[a1] = self.query_fn(self.tree[a1 * 2], self.tree[a1 * 2 + 1])
                if self.lazy[a1] is not None:
                    self.tree[a1] = self.update_fn(self.tree[a1], self.lazy[a1])
        a1 += self.N
        a2 += self.N
        v3, v4 = (a1, a2)
        while a1 <= a2:
            if a1 & 1:
                self.__apply(a1, a3)
                a1 += 1
            if a2 & 1 == 0:
                self.__apply(a2, a3)
                a2 -= 1
            a1 //= 2
            a2 //= 2
        pull(v3)
        pull(v4)

    def query(self, a1, a2):

        def push(a1):
            v1 = 2 ** self.H
            while v1 != 1:
                v2 = a1 // v1
                if self.lazy[v2] is not None:
                    self.__apply(v2 * 2, self.lazy[v2])
                    self.__apply(v2 * 2 + 1, self.lazy[v2])
                    self.lazy[v2] = None
                v1 //= 2
        v1 = self.default_val
        if a1 > a2:
            return v1
        a1 += self.N
        a2 += self.N
        push(a1)
        push(a2)
        while a1 <= a2:
            if a1 & 1:
                v1 = self.query_fn(v1, self.tree[a1])
                a1 += 1
            if a2 & 1 == 0:
                v1 = self.query_fn(v1, self.tree[a2])
                a2 -= 1
            a1 //= 2
            a2 //= 2
        return v1

    def __str__(self):
        v1 = []
        for v2 in range(self.N):
            v1.append(self.query(v2, v2))
        return ','.join(map(str, v1))
