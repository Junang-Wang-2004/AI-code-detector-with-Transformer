import collections
from collections import defaultdict

class C1:

    def alienOrder(self, a1):
        v1 = set((c for v2 in a1 for v3 in v2))
        if not v1:
            return ''
        v4 = defaultdict(list)
        v5 = {v3: 0 for v3 in v1}
        for v6 in range(1, len(a1)):
            v7, v8 = (a1[v6 - 1], a1[v6])
            if len(v7) > len(v8) and v7[:len(v8)] == v8:
                return ''
            for v9 in range(min(len(v7), len(v8))):
                if v7[v9] != v8[v9]:
                    v10, v11 = (v7[v9], v8[v9])
                    if v11 not in v4[v10]:
                        v4[v10].append(v11)
                        v5[v11] += 1
                    break
        v12 = collections.deque((v3 for v3 in v1 if v5[v3] == 0))
        v13 = []
        while v12:
            v14 = v12.popleft()
            v13.append(v14)
            for v15 in v4[v14]:
                v5[v15] -= 1
                if v5[v15] == 0:
                    v12.append(v15)
        return ''.join(v13) if len(v13) == len(v1) else ''
