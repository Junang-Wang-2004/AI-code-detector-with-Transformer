import collections
from collections import deque

class C1(object):

    def minJumps(self, a1):
        v1 = len(a1)
        v2 = collections.defaultdict(list)
        for v3, v4 in enumerate(a1):
            v2[v4].append(v3)
        v5 = set([0])
        v6 = deque([(0, 0)])
        v7 = set()
        while v6:
            v8, v9 = v6.popleft()
            if v8 == v1 - 1:
                return v9
            for v10 in [-1, 1]:
                v11 = v8 + v10
                if 0 <= v11 < v1 and v11 not in v5:
                    v5.add(v11)
                    v6.append((v11, v9 + 1))
            v12 = a1[v8]
            if v12 not in v7:
                v7.add(v12)
                for v13 in v2[v12]:
                    if v13 not in v5:
                        v5.add(v13)
                        v6.append((v13, v9 + 1))
