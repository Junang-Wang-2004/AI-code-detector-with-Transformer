import collections

class C1(object):

    def catMouseGame(self, a1):
        """
        """
        v1, v2, v3 = list(range(3))
        v4, v5, v6 = list(range(3))

        def parents(a1, a2, a3):
            if a3 == v6:
                for v1 in a1[a1]:
                    yield (v1, a2, v5 ^ v6 ^ a3)
            else:
                for v2 in a1[a2]:
                    if v2 != v1:
                        yield (a1, v2, v5 ^ v6 ^ a3)
        v7 = {}
        v8 = set(a1[v1])
        for v9 in range(len(a1)):
            for v10 in range(len(a1)):
                v7[v9, v10, v5] = len(a1[v9])
                v7[v9, v10, v6] = len(a1[v10]) - (v10 in v8)
        v11 = collections.defaultdict(int)
        v12 = collections.deque()
        for v13 in range(len(a1)):
            if v13 == v1:
                continue
            v11[v1, v13, v6] = v5
            v12.append((v1, v13, v6, v5))
            for v14 in [v5, v6]:
                v11[v13, v13, v14] = v6
                v12.append((v13, v13, v14, v6))
        while v12:
            v13, v15, v14, v10 = v12.popleft()
            for v16, v17, v18 in parents(v13, v15, v14):
                if v11[v16, v17, v18] != v4:
                    continue
                if v18 == v10:
                    v11[v16, v17, v18] = v10
                    v12.append((v16, v17, v18, v10))
                    continue
                v7[v16, v17, v18] -= 1
                if not v7[v16, v17, v18]:
                    v11[v16, v17, v18] = v10
                    v12.append((v16, v17, v18, v10))
        return v11[v2, v3, v5]
