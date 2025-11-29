import bisect

class C1(object):

    def fallingSquares(self, a1):
        v1 = []
        v2 = [-1]
        v3 = [0]
        v4 = 0
        for v5, v6 in a1:
            v7 = bisect.bisect_right(v2, v5)
            v8 = bisect.bisect_left(v2, v5 + v6)
            v9 = max(v3[v7 - 1:v8] or [0]) + v6
            v2[v7:v8] = [v5, v5 + v6]
            v3[v7:v8] = [v9, v3[v8 - 1]]
            v4 = max(v4, v9)
            v1.append(v4)
        return v1

class C2(object):

    def __init__(self, a1, a2=min, a3=lambda x, y: y, a4=float('inf')):
        self.N = a1
        self.H = (a1 - 1).bit_length()
        self.query_fn = a2
        self.update_fn = a3
        self.default_val = a4
        self.tree = [a4] * (2 * a1)
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

    def data(self):
        v1 = []
        for v2 in range(self.N):
            v1.append(self.query(v2, v2))
        return v1

class C3(object):

    def __init__(self, a1, a2=min, a3=lambda x, y: y, a4=float('inf')):
        """
        initialize your data structure here.
        """
        v1 = len(a1)
        self.__original_length = v1
        self.__tree_length = 2 ** (v1.bit_length() + (v1 & v1 - 1 != 0)) - 1
        self.__query_fn = a2
        self.__update_fn = a3
        self.__default_val = a4
        self.__tree = [a4 for v2 in range(self.__tree_length)]
        self.__lazy = [None for v2 in range(self.__tree_length)]
        self.__constructTree(a1, 0, self.__original_length - 1, 0)

    def update(self, a1, a2, a3):
        self.__updateTree(a3, a1, a2, 0, self.__original_length - 1, 0)

    def query(self, a1, a2):
        return self.__queryRange(a1, a2, 0, self.__original_length - 1, 0)

    def __constructTree(self, a1, a2, a3, a4):
        if a2 > a3:
            return
        if a2 == a3:
            self.__tree[a4] = self.__update_fn(self.__tree[a4], a1[a2])
            return
        v1 = a2 + (a3 - a2) // 2
        self.__constructTree(a1, a2, v1, a4 * 2 + 1)
        self.__constructTree(a1, v1 + 1, a3, a4 * 2 + 2)
        self.__tree[a4] = self.__query_fn(self.__tree[a4 * 2 + 1], self.__tree[a4 * 2 + 2])

    def __apply(self, a1, a2, a3, a4):
        self.__tree[a3] = self.__update_fn(self.__tree[a3], a4)
        if a1 != a2:
            self.__lazy[a3 * 2 + 1] = self.__update_fn(self.__lazy[a3 * 2 + 1], a4)
            self.__lazy[a3 * 2 + 2] = self.__update_fn(self.__lazy[a3 * 2 + 2], a4)

    def __updateTree(self, a1, a2, a3, a4, a5, a6):
        if a4 > a5:
            return
        if self.__lazy[a6] is not None:
            self.__apply(a4, a5, a6, self.__lazy[a6])
            self.__lazy[a6] = None
        if a2 > a5 or a3 < a4:
            return
        if a2 <= a4 and a5 <= a3:
            self.__apply(a4, a5, a6, a1)
            return
        v1 = a4 + (a5 - a4) // 2
        self.__updateTree(a1, a2, a3, a4, v1, a6 * 2 + 1)
        self.__updateTree(a1, a2, a3, v1 + 1, a5, a6 * 2 + 2)
        self.__tree[a6] = self.__query_fn(self.__tree[a6 * 2 + 1], self.__tree[a6 * 2 + 2])

    def __queryRange(self, a1, a2, a3, a4, a5):
        if a3 > a4:
            return self.__default_val
        if self.__lazy[a5] is not None:
            self.__apply(a3, a4, a5, self.__lazy[a5])
            self.__lazy[a5] = None
        if a4 < a1 or a3 > a2:
            return self.__default_val
        if a1 <= a3 and a4 <= a2:
            return self.__tree[a5]
        v1 = a3 + (a4 - a3) // 2
        return self.__query_fn(self.__queryRange(a1, a2, a3, v1, a5 * 2 + 1), self.__queryRange(a1, a2, v1 + 1, a4, a5 * 2 + 2))
