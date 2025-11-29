class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.rank = [0] * a1

    def find(self, a1):
        if self.parent[a1] != a1:
            self.parent[a1] = self.find(self.parent[a1])
        return self.parent[a1]

    def unite(self, a1, a2):
        v1 = self.find(a1)
        v2 = self.find(a2)
        if v1 == v2:
            return False
        if self.rank[v1] < self.rank[v2]:
            self.parent[v1] = v2
        elif self.rank[v1] > self.rank[v2]:
            self.parent[v2] = v1
        else:
            self.parent[v2] = v1
            self.rank[v1] += 1
        return True

class C2:

    def findMedian(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = len(a3)
        v7 = [[] for v2 in range(a1)]
        for v8, (v9, v10) in enumerate(a3):
            v7[v9].append(v8)
            v7[v10].append(v8)
        v11 = C1(a1)
        v12 = list(range(a1))
        v13 = [0] * a1
        v14 = [0] * a1
        v15 = [0] * v6
        v16 = [0] * v6
        v17 = [False] * a1

        def first_dfs(a1):
            for v1 in v7[a1]:
                v2, v3 = a3[v1]
                if v2 == v3:
                    v16[v1] = a1
                    continue
                v15[v1] += v13[a1]
                v4 = v2 if a1 == v3 else v3
                if v17[v4]:
                    v5 = v11.find(v4)
                    v16[v1] = v12[v5]
                    v15[v1] -= 2 * v13[v16[v1]]
            v17[a1] = True
            for v6, v7 in v1[a1]:
                if v17[v6]:
                    continue
                v13[v6] = v13[a1] + v7
                v14[v6] = v14[a1] + 1
                first_dfs(v6)
                v11.unite(v6, a1)
                v12[v11.find(a1)] = a1
        first_dfs(0)
        v18 = [[] for v2 in range(a1)]
        for v8 in range(v6):
            v3, v4 = a3[v8]
            v19 = v13[v3] - v13[v16[v8]]
            if 2 * v19 >= v15[v8]:
                v18[v3].append((v8, 0))
            else:
                v18[v4].append((v8, 1))
        v20 = [0] * v6
        v21 = []

        def bs(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1

        def sec_dfs(a1):
            v21.append(a1)
            for v1, v2 in v18[a1]:
                v3 = v16[v1]
                v4 = v14[a1] - v14[v3]
                v5 = v15[v1]
                if v2 == 0:

                    def cond(a1):
                        v1 = v21[-(a1 + 1)]
                        v2 = v13[a1] - v13[v1]
                        return 2 * v2 >= v5
                    v6 = bs(0, v4, cond)
                    v20[v1] = v21[-(v6 + 1)]
                else:
                    v7 = v13[a3[v1][0]] - v13[v3]

                    def cond(a1):
                        v1 = v21[-v4 + a1]
                        v2 = v13[v1] - v13[v3]
                        v3 = v7 + v2
                        return 2 * v3 >= v5
                    v6 = bs(0, v4 - 1, cond)
                    v20[v1] = v21[-v4 + v6]
            for v8, v9 in v1[a1]:
                if len(v21) >= 2 and v21[-2] == v8:
                    continue
                sec_dfs(v8)
            v21.pop()
        sec_dfs(0)
        return v20
