class FenwickTree:
    def __init__(self, size):
        self._n = size
        self._tree = [0] * (size + 2)

    def _update(self, idx, delta):
        idx += 1
        while idx <= self._n + 1:
            self._tree[idx] += delta
            idx += idx & -idx

    def _query(self, idx):
        idx += 1
        res = 0
        while idx:
            res += self._tree[idx]
            idx -= idx & -idx
        return res

    def find_kth(self, k):
        left = 0
        right = self._n - 1
        while left < right:
            mid = (left + right) // 2
            if self._query(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left


class MRUQueue:
    def __init__(self, n):
        EXTRA = 5000
        self._ft = FenwickTree(n + EXTRA)
        self._pos_to_val = {}
        self._next_pos = n
        for i in range(n):
            self._pos_to_val[i] = i + 1
            self._ft._update(i, 1)

    def fetch(self, k):
        idx = self._ft.find_kth(k)
        num = self._pos_to_val.pop(idx)
        self._ft._update(idx, -1)
        self._ft._update(self._next_pos, 1)
        self._pos_to_val[self._next_pos] = num
        self._next_pos += 1
        return num
