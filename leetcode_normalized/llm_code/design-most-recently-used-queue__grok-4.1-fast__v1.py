class C1:

    def __init__(self, a1):
        self._n = a1
        self._tree = [0] * (a1 + 2)

    def _update(self, a1, a2):
        a1 += 1
        while a1 <= self._n + 1:
            self._tree[a1] += a2
            a1 += a1 & -a1

    def _query(self, a1):
        a1 += 1
        v2 = 0
        while a1:
            v2 += self._tree[a1]
            a1 -= a1 & -a1
        return v2

    def find_kth(self, a1):
        v1 = 0
        v2 = self._n - 1
        while v1 < v2:
            v3 = (v1 + v2) // 2
            if self._query(v3) >= a1:
                v2 = v3
            else:
                v1 = v3 + 1
        return v1

class C2:

    def __init__(self, a1):
        v1 = 5000
        self._ft = C1(a1 + v1)
        self._pos_to_val = {}
        self._next_pos = a1
        for v2 in range(a1):
            self._pos_to_val[v2] = v2 + 1
            self._ft._update(v2, 1)

    def fetch(self, a1):
        v1 = self._ft.find_kth(a1)
        v2 = self._pos_to_val.pop(v1)
        self._ft._update(v1, -1)
        self._ft._update(self._next_pos, 1)
        self._pos_to_val[self._next_pos] = v2
        self._next_pos += 1
        return v2
