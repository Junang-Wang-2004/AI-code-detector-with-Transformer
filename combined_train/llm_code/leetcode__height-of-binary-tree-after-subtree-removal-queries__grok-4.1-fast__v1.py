import collections
from typing import List

class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def treeQueries(self, a1: C1, a2: List[int]) -> List[int]:
        v1 = {}
        v2 = {}
        v3 = collections.defaultdict(int)
        v4 = collections.defaultdict(int)

        def measure(a1, a2):
            if not a1:
                return 0
            v1 = measure(a1.left, a2 + 1)
            v2 = measure(a1.right, a2 + 1)
            v3 = 1 + max(v1, v2)
            v1[a1.val] = a2
            v2[a1.val] = v3
            if v3 > v3[a2]:
                v4[a2] = v3[a2]
                v3[a2] = v3
            elif v3 > v4[a2]:
                v4[a2] = v3
            return v3
        if a1:
            measure(a1, 0)
        v5 = []
        for v6 in a2:
            v7 = v1[v6]
            v8 = v2[v6]
            v9 = v4[v7] if v8 == v3[v7] else v3[v7]
            v5.append(v7 - 1 + v9)
        return v5
