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
        v7 = collections.defaultdict(int)
        v8 = {}
        v9 = set(a1[v1])
        for v10 in range(len(a1)):
            for v11 in range(len(a1)):
                v8[v10, v11, v5] = len(a1[v10])
                v8[v10, v11, v6] = len(a1[v11]) - (v11 in v9)
        v12 = collections.deque()
        v13 = collections.deque()
        for v14 in range(len(a1)):
            if v14 == v1:
                continue
            v7[v1, v14, v6] = v5
            v12.append((v1, v14, v6))
            for v15 in [v5, v6]:
                v7[v14, v14, v15] = v6
                v13.append((v14, v14, v15))
        while v12:
            v14, v16, v15 = v12.popleft()
            for v17, v18, v19 in parents(v14, v16, v15):
                if v7[v17, v18, v19] != v4:
                    continue
                if v15 == v6:
                    v7[v17, v18, v19] = v5
                    v12.append((v17, v18, v19))
                    continue
                v8[v17, v18, v19] -= 1
                if not v8[v17, v18, v19]:
                    v7[v17, v18, v19] = v5
                    v12.append((v17, v18, v19))
        while v13:
            v14, v16, v15 = v13.popleft()
            for v17, v18, v19 in parents(v14, v16, v15):
                if v7[v17, v18, v19] != v4:
                    continue
                if v15 == v5:
                    v7[v17, v18, v19] = v6
                    v13.append((v17, v18, v19))
                    continue
                v8[v17, v18, v19] -= 1
                if not v8[v17, v18, v19]:
                    v7[v17, v18, v19] = v6
                    v13.append((v17, v18, v19))
        return v7[v2, v3, v5]
