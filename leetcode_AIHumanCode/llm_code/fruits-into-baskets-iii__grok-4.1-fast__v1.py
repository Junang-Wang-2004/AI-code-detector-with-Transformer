class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        class SegTree:
            def __init__(self, data):
                self.size = len(data)
                self.tree = [0] * (4 * self.size)
                if self.size > 0:
                    self._construct(1, 0, self.size - 1, data)

            def _construct(self, v, l, r, data):
                if l == r:
                    self.tree[v] = data[l]
                    return
                m = (l + r) // 2
                self._construct(2 * v, l, m, data)
                self._construct(2 * v + 1, m + 1, r, data)
                self.tree[v] = max(self.tree[2 * v], self.tree[2 * v + 1])

            def _modify(self, v, l, r, pos, new_val):
                if l == r:
                    self.tree[v] = new_val
                    return
                m = (l + r) // 2
                if pos <= m:
                    self._modify(2 * v, l, m, pos, new_val)
                else:
                    self._modify(2 * v + 1, m + 1, r, pos, new_val)
                self.tree[v] = max(self.tree[2 * v], self.tree[2 * v + 1])

            def find_first_ge(self, v, l, r, val):
                if self.tree[v] < val:
                    return -1
                if l == r:
                    return l
                m = (l + r) // 2
                res = self.find_first_ge(2 * v, l, m, val)
                if res != -1:
                    return res
                return self.find_first_ge(2 * v + 1, m + 1, r, val)

        if not baskets:
            return len(fruits)
        tree = SegTree(baskets)
        unplaced = 0
        for size in fruits:
            pos = tree.find_first_ge(1, 0, tree.size - 1, size)
            if pos == -1:
                unplaced += 1
            else:
                tree._modify(1, 0, tree.size - 1, pos, 0)
        return unplaced
