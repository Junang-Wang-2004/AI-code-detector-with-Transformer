import operator

class C1:

    def __init__(self, a1, a2=operator.add, a3=None, a4=None):
        """
        :param int size:
        :param callable fn: 区間に適用する関数。引数を 2 つ取る。min, max, operator.xor など
        :param default:
        :param list initial_values:
        """
        a3 = a3 or 0
        v2 = 1
        while v2 < a1:
            v2 *= 2
        self._size = v2
        self._fn = a2
        self._tree = [a3] * (self._size * 2 - 1)
        if a4:
            v3 = self._size - 1
            for v4 in a4:
                self._tree[v3] = v4
                v3 += 1
            v3 = self._size - 2
            while v3 >= 0:
                self._tree[v3] = self._fn(self._tree[v3 * 2 + 1], self._tree[v3 * 2 + 2])
                v3 -= 1

    def set(self, a1, a2):
        """
        i 番目に value を設定
        :param int i:
        :param value:
        :return:
        """
        v1 = self._size - 1 + a1
        self._tree[v1] = a2
        while v1 > 0:
            v1 = (v1 - 1) // 2
            self._tree[v1] = self._fn(self._tree[v1 * 2 + 1], self._tree[v1 * 2 + 2])

    def add(self, a1, a2):
        """
        もとの i 番目と value に fn を適用したものを i 番目に設定
        :param int i:
        :param value:
        :return:
        """
        v1 = self._size - 1 + a1
        self.set(a1, self._fn(self._tree[v1], a2))

    def get(self, a1, a2=None, a3=0, a4=None, a5=None):
        """
        [from_i, to_i) に fn を適用した結果を返す
        :param int from_i:
        :param int to_i:
        :param int k: self._tree[k] が、[L, r) に fn を適用した結果を持つ
        :param int L:
        :param int r:
        :return:
        """
        if a2 is None:
            return self._tree[self._size - 1 + a1]
        a4 = 0 if a4 is None else a4
        a5 = self._size if a5 is None else a5
        if a1 <= a4 and a5 <= a2:
            return self._tree[a3]
        if a2 <= a4 or a5 <= a1:
            return None
        v3 = self.get(a1, a2, a3 * 2 + 1, a4, (a4 + a5) // 2)
        v4 = self.get(a1, a2, a3 * 2 + 2, (a4 + a5) // 2, a5)
        if v3 is None:
            return v4
        if v4 is None:
            return v3
        return self._fn(v3, v4)

    def __len__(self):
        return self._size
from bisect import bisect_right

def f4():
    v1, v2, v3 = map(int, input().split())
    v4 = [list(map(int, input().split())) for v5 in range(v1)]
    v4.sort()
    v6, v5 = zip(*v4)
    v2 = 2 * v2
    v7 = C1(v1 + 10)
    v8 = 0
    for v9, (v10, v11) in enumerate(v4):
        v11 = -(-v11 // v3)
        v12 = v7.get(0, v9 + 1)
        if v11 < v12:
            continue
        v8 += v11 - v12
        v7.add(v9, v11 - v12)
        v7.add(bisect_right(v6, v10 + v2), -v11 + v12)
    print(v8)
if __name__ == '__main__':
    f4()
