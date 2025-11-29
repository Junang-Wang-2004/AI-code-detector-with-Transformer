from sortedcontainers import SortedList

class C1(object):

    def amountPainted(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, (v3, v4) in enumerate(a1):
            v1[v3].append((True, v2))
            v1[v4].append((False, v2))
        v5 = SortedList()
        v6 = [0] * len(a1)
        v7 = -1
        for v8 in sorted(v1.keys()):
            if v5:
                v6[v5[0]] += v8 - v7
            v7 = v8
            for v9, v2 in v1[v8]:
                if v9:
                    v5.add(v2)
                else:
                    v5.remove(v2)
        return v6

class C2(object):

    def __init__(self, a1, a2=lambda x: 0, a3=lambda x, y: y if x is None else x + y, a4=lambda x, y: y):
        self.tree = [None] * (2 * a1)
        self.lazy = [None] * len(self.tree)
        self.base = len(self.tree) // 2
        self.H = (self.base - 1).bit_length()
        self.query_fn = a3
        self.update_fn = a4
        for v1 in range(self.base, self.base + a1):
            self.tree[v1] = a2(v1 - self.base)
        for v1 in reversed(range(1, self.base)):
            self.tree[v1] = a3(self.tree[2 * v1], self.tree[2 * v1 + 1])
        self.count = [1] * (2 * a1)
        for v1 in reversed(range(1, a1)):
            self.count[v1] = self.count[2 * v1] + self.count[2 * v1 + 1]

    def __apply(self, a1, a2):
        self.tree[a1] = self.update_fn(self.tree[a1], a2 * self.count[a1])
        if a1 < self.base:
            self.lazy[a1] = self.update_fn(self.lazy[a1], a2)

    def __push(self, a1):
        v1 = 2 ** self.H
        while v1 != 1:
            v2 = a1 // v1
            if self.lazy[v2] is not None:
                self.__apply(v2 * 2, self.lazy[v2])
                self.__apply(v2 * 2 + 1, self.lazy[v2])
                self.lazy[v2] = None
            v1 //= 2

    def update(self, a1, a2, a3):

        def pull(a1):
            while a1 > 1:
                a1 //= 2
                self.tree[a1] = self.query_fn(self.tree[a1 * 2], self.tree[a1 * 2 + 1])
                if self.lazy[a1] is not None:
                    self.tree[a1] = self.update_fn(self.tree[a1], self.lazy[a1] * self.count[a1])
        if a1 > a2:
            return
        a1 += self.base
        a2 += self.base
        self.__push(a1)
        self.__push(a2)
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
        v1 = None
        if a1 > a2:
            return v1
        a1 += self.base
        a2 += self.base
        self.__push(a1)
        self.__push(a2)
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
