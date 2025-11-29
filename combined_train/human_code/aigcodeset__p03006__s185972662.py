import itertools
import os
import sys
if os.getenv('LOCAL'):
    sys.stdin = open('_in.txt', 'r')
sys.setrecursionlimit(2147483647)
v1 = float('inf')

class C1:

    def __init__(self, a1=None, a2=None):
        """
        size か nodes どっちか指定。
        nodes は set、size は list を使う。
        set の最悪計算量は O(N) なので size 指定のほうが若干速い
        :param int size:
        :param collections.Iterable nodes:
        """
        assert a1 is not None or a2 is not None
        if a1 is not None:
            self._parents = [i for v1 in range(a1)]
            self._ranks = [0 for v2 in range(a1)]
            self._sizes = [1 for v2 in range(a1)]
        else:
            self._parents = {k: k for v3 in a2}
            self._ranks = {v3: 0 for v3 in a2}
            self._sizes = {v3: 1 for v3 in a2}

    def unite(self, a1, a2):
        """
        x が属する木と y が属する木を併合
        :param x:
        :param y:
        :return:
        """
        a1 = self.find(a1)
        a2 = self.find(a2)
        if a1 == a2:
            return
        if self._ranks[a1] > self._ranks[a2]:
            self._parents[a2] = a1
            self._sizes[a1] += self._sizes[a2]
        else:
            self._parents[a1] = a2
            self._sizes[a2] += self._sizes[a1]
            if self._ranks[a1] == self._ranks[a2]:
                self._ranks[a2] += 1

    def find(self, a1):
        """
        x が属する木の root
        :param x:
        :return:
        """
        if self._parents[a1] == a1:
            return a1
        self._parents[a1] = self.find(self._parents[a1])
        return self._parents[a1]

    def size(self, a1):
        """
        x が属する木のノード数
        :param x:
        :return:
        """
        return self._sizes[self.find(a1)]
v2 = int(sys.stdin.readline())
v3, v4 = list(zip(*[map(int, sys.stdin.readline().split()) for v5 in range(v2)]))
v6 = min(v3)
v7 = min(v4)
v8 = max(v3)
v9 = max(v4)
v10 = {}
for v11, (v12, v13) in enumerate(zip(v3, v4)):
    v10[v12, v13] = v11
v14 = v2
for v11, v15 in itertools.combinations(range(v2), r=2):
    v16, v17 = (v3[v11], v3[v15])
    v18, v19 = (v4[v11], v4[v15])
    v20 = v16 - v17
    v21 = v18 - v19
    v22 = C1(size=v2)
    for v23 in range(v2):
        v12, v13 = (v3[v23], v4[v23])
        if (v12 + v20, v13 + v21) in v10:
            v22.unite(v23, v10[v12 + v20, v13 + v21])
        if (v12 - v20, v13 - v21) in v10:
            v22.unite(v23, v10[v12 - v20, v13 - v21])
    v24 = set()
    for v23 in range(v2):
        v24.add(v22.find(v23))
    v14 = min(len(v24), v14)
print(v14)
