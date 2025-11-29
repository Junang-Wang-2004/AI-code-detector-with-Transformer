import bisect

class C1(object):

    def __init__(self, a1, a2, a3):
        self.tree = [None] * (2 * 2 ** (a1 - 1).bit_length())
        self.base = len(self.tree) // 2
        self.query_fn = a3
        for v1 in range(self.base, self.base + a1):
            self.tree[v1] = a2(v1 - self.base)
        for v1 in reversed(range(1, self.base)):
            self.tree[v1] = a3(self.tree[2 * v1], self.tree[2 * v1 + 1])

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

def f2(a1):
    v1 = []
    v2 = [-1] * (a1 + 1)
    for v3 in range(2, a1 + 1):
        if v2[v3] == -1:
            v2[v3] = v3
            v1.append(v3)
        for v4 in v1:
            if v3 * v4 > a1 or v4 > v2[v3]:
                break
            v2[v3 * v4] = v4
    return v1
v1 = 10 ** 6
v2 = f2(v1)
v3 = C1(len(v2) - 1, build_fn=lambda i: [v2[i + 1] - v2[i], [v2[i], v2[i + 1]]], query_fn=lambda x, y: y if x is None else x if y is None else min(x, y))

class C2(object):

    def closestPrimes(self, a1, a2):
        """
        """
        v1 = bisect.bisect_left(v2, a1)
        v2 = bisect.bisect_right(v2, a2) - 1
        return v3.query(v1, v2 - 1)[1] if v1 <= v2 - 1 else [-1] * 2
