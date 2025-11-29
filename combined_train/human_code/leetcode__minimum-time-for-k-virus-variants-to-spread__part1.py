class C1(object):

    def __init__(self, a1, a2=lambda x, y: [y] * (2 * x), a3=lambda x, y: y if x is None else max(x, y), a4=lambda x, y: y if x is None else x + y, a5=0):
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
        v1 = None
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

class C2(object):

    def minDayskVariants(self, a1, a2):
        """
        """

        def add_rec(a1, a2):
            v1, v2, v3, v4 = a1
            a2.append([[v1, +1], [v2, v4]])
            a2.append([[v3 + 1, -1], [v2, v4]])

        def check(a1, a2, a3):
            v1 = []
            v2 = set()
            for v3, v4 in a1:
                add_rec([v3 - a3, v4 - a3, v3 + a3, v4 + a3], v1)
                v2.add(v4 - a3)
                v2.add(v4 + a3)
            v1.sort()
            v5 = {v4: i for v6, v4 in enumerate(sorted(v2))}
            v7 = C1(len(v5))
            for [v8, v9], [v10, v11] in v1:
                v7.update(v5[v10], v5[v11], v9)
                if v7.query(0, len(v5) - 1) >= a2:
                    return True
            return False
        a1 = [[x + y, x - y] for v2, v3 in a1]
        v4 = min(a1)[0]
        v5 = max(a1)[0]
        v6 = min(a1, key=lambda x: v2[1])[1]
        v7 = max(a1, key=lambda x: v2[1])[1]
        v8, v9 = (0, (v5 - v4 + (v7 - v6) + 1) // 2)
        while v8 <= v9:
            v10 = v8 + (v9 - v8) // 2
            if check(a1, a2, v10):
                v9 = v10 - 1
            else:
                v8 = v10 + 1
        return v8
