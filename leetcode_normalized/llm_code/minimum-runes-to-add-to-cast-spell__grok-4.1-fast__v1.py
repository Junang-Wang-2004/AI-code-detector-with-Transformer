class C1(object):

    def minRunesToAdd(self, a1, a2, a3, a4):
        v1 = [[] for v2 in range(a1)]
        for v3 in range(len(a3)):
            v1[a3[v3]].append(a4[v3])
        v4 = [[] for v2 in range(a1)]
        for v5 in range(a1):
            for v6 in v1[v5]:
                v4[v6].append(v5)
        v7 = [False] * a1
        v8 = []

        def dfs_first(a1):
            v7[a1] = True
            for v1 in v1[a1]:
                if not v7[v1]:
                    dfs_first(v1)
            v8.append(a1)
        for v9 in range(a1):
            if not v7[v9]:
                dfs_first(v9)
        v7 = [False] * a1
        v10 = [-1] * a1
        v11 = 0

        def dfs_second(a1, a2):
            v7[a1] = True
            v10[a1] = a2
            for v1 in v4[a1]:
                if not v7[v1]:
                    dfs_second(v1, a2)
        for v9 in v8[::-1]:
            if not v7[v9]:
                dfs_second(v9, v11)
                v11 += 1
        v12 = [True] * v11
        for v13 in a2:
            v12[v10[v13]] = False
        for v14 in range(a1):
            for v15 in v1[v14]:
                if v10[v14] != v10[v15]:
                    v12[v10[v15]] = False
        return sum(v12)
