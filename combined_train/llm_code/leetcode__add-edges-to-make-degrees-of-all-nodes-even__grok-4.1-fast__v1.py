class C1(object):

    def isPossible(self, a1, a2):
        v1 = [set() for v2 in range(a1)]
        for v3, v4 in a2:
            v5 = v3 - 1
            v6 = v4 - 1
            v1[v5].add(v6)
            v1[v6].add(v5)
        v7 = [i for v8 in range(a1) if len(v1[v8]) % 2 == 1]
        v9 = len(v7)
        if v9 == 0:
            return True
        if v9 not in (2, 4):
            return False
        if v9 == 2:
            v10, v11 = v7
            v12 = v1[v10]
            v13 = v1[v11]
            if v11 not in v12:
                return True
            v14 = v12.union(v13)
            return len(v14) < a1
        v15, v16, v17, v18 = v7
        v19 = [v18 not in v1[v15] and v17 not in v1[v16], v17 not in v1[v15] and v18 not in v1[v16], v16 not in v1[v15] and v17 not in v1[v18]]
        return any(v19)
