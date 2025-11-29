class C1(object):

    def __init__(self, a1, a2=lambda _: float('inf'), a3=lambda x, y: y if x is None else x if y is None else min(x, y), a4=lambda x: x):
        self.tree = [None] * (2 * 2 ** (a1 - 1).bit_length())
        self.base = len(self.tree) // 2
        self.query_fn = a3
        self.update_fn = a4
        for v1 in range(self.base, self.base + a1):
            self.tree[v1] = a2(v1 - self.base)
        for v1 in reversed(range(1, self.base)):
            self.tree[v1] = a3(self.tree[2 * v1], self.tree[2 * v1 + 1])

    def update(self, a1, a2):
        v1 = self.base + a1
        self.tree[v1] = self.update_fn(a2)
        while v1 > 1:
            v1 //= 2
            self.tree[v1] = self.query_fn(self.tree[v1 * 2], self.tree[v1 * 2 + 1])

    def query(self, a1, a2):
        a1 += self.base
        a2 += self.base
        v3 = v4 = None
        while a1 <= a2:
            if a1 & 1:
                v3 = self.query_fn(v3, self.tree[a1])
                a1 += 1
            if a2 & 1 == 0:
                v4 = self.query_fn(self.tree[a2], v4)
                a2 -= 1
            a1 //= 2
            a2 //= 2
        return self.query_fn(v3, v4)

class C2(object):

    def __init__(self, a1, a2):
        """
        """
        self.__st = C1(a1, build_fn=lambda _: [a2] * 2, query_fn=lambda x, y: y if x is None else x if y is None else [max(x[0], y[0]), x[1] + y[1]])
        self.__m = a2
        self.__i = 0

    def gather(self, a1, a2):
        """
        """
        v1 = 1
        if a1 > self.__st.tree[v1][0]:
            return []
        while v1 < self.__st.base:
            v1 = 2 * v1 + int(self.__st.tree[2 * v1][0] < a1)
        if v1 - self.__st.base > a2:
            return []
        v2 = self.__st.tree[v1][0]
        v3 = self.__m - v2
        v1 -= self.__st.base
        self.__st.update(v1, [v2 - a1] * 2)
        return [v1, v3]

    def scatter(self, a1, a2):
        """
        """
        v1 = self.__st.query(self.__i, a2)
        if not v1 or v1[1] < a1:
            return False
        for v2 in range(self.__i, a2 + 1):
            v1 = self.__st.tree[self.__st.base + v2][1]
            v3 = min(v1, a1)
            v1 -= v3
            if not v1:
                self.__i += 1
            self.__st.update(v2, [v1] * 2)
            a1 -= v3
            if not a1:
                break
        return True
