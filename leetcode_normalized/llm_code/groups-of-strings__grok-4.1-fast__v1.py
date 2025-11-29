from collections import Counter

class C1:

    def groupStrings(self, a1):
        v1 = Counter()
        for v2 in a1:
            v3 = 0
            for v4 in v2:
                v3 |= 1 << ord(v4) - ord('a')
            v1[v3] += 1
        v5 = list(v1)
        v6 = len(v5)
        v7 = {v5[j]: j for v8 in range(v6)}

        class DSU:

            def __init__(self, a1):
                self.pr = list(range(a1))
                self.rk = [0] * a1
                self.sz = [v1[v5[v8]] for v8 in range(a1)]

            def get(self, a1):
                if self.pr[a1] != a1:
                    self.pr[a1] = self.get(self.pr[a1])
                return self.pr[a1]

            def merge(self, a1, a2):
                v1 = self.get(a1)
                v2 = self.get(a2)
                if v1 == v2:
                    return
                if self.rk[v1] < self.rk[v2]:
                    self.pr[v1] = v2
                    self.sz[v2] += self.sz[v1]
                elif self.rk[v1] > self.rk[v2]:
                    self.pr[v2] = v1
                    self.sz[v1] += self.sz[v2]
                else:
                    self.pr[v2] = v1
                    self.sz[v1] += self.sz[v2]
                    self.rk[v1] += 1
        if v6 == 0:
            return [0, 0]
        v9 = DSU(v6)
        for v10 in range(v6):
            v11 = v5[v10]
            for v12 in range(26):
                v13 = 1 << v12
                if v11 & v13:
                    v14 = v11 ^ v13
                    if v14 in v7:
                        v9.merge(v10, v7[v14])
        v15 = set()
        v16 = 0
        v17 = 0
        for v10 in range(v6):
            v18 = v9.get(v10)
            if v18 not in v15:
                v15.add(v18)
                v16 += 1
                v17 = max(v17, v9.sz[v18])
        return [v16, v17]
