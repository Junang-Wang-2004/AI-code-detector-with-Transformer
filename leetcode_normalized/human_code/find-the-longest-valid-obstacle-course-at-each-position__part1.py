import bisect

class C1(object):

    def longestObstacleCourseAtEachPosition(self, a1):
        """
        """
        v1, v2 = ([], [])
        for v3 in a1:
            v4 = bisect.bisect_right(v2, v3)
            v1.append(v4 + 1)
            if v4 == len(v2):
                v2.append(0)
            v2[v4] = v3
        return v1

class C2(object):

    def __init__(self, a1, a2=lambda x, y: [y] * (2 * x), a3=lambda x, y: y if x is None else max(x, y), a4=lambda x, y: y, a5=0):
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
