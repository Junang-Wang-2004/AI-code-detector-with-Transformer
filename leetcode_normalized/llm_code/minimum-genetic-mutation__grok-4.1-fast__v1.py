from collections import deque

class C1:

    def minMutation(self, a1, a2, a3):
        v1 = set(a3)
        v2 = set([a1])
        v3 = deque([(a1, 0)])
        while v3:
            v4, v5 = v3.popleft()
            if v4 == a2:
                return v5
            for v6 in range(len(v4)):
                v7 = v4[v6]
                for v8 in 'ATCG':
                    if v8 == v7:
                        continue
                    v9 = list(v4)
                    v9[v6] = v8
                    v10 = ''.join(v9)
                    if v10 in v1 and v10 not in v2:
                        v2.add(v10)
                        v3.append((v10, v5 + 1))
        return -1
