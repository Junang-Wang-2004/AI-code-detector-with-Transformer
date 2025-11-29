import collections

class C1(object):

    def supersequences(self, a1):
        v1 = sorted(set((c for v2 in a1 for v3 in v2)))
        v4 = len(v1)
        if v4 == 0:
            return [[0] * 26]
        v5 = {v1[i]: i for v6 in range(v4)}
        v7 = [[] for v8 in range(v4)]
        v9 = [0] * v4
        for v2 in a1:
            v10 = v5[v2[0]]
            v11 = v5[v2[1]]
            v7[v10].append(v11)
            v9[v11] += 1
        v12 = float('inf')
        v13 = []
        for v14 in range(1 << v4):
            v15 = [1 + (v14 >> j & 1) for v16 in range(v4)]
            v17 = sum(v15)
            if v17 > v12:
                continue
            v18 = v15[:]
            v19 = v9[:]
            v20 = [False] * v4
            v21 = collections.deque()
            for v22 in range(v4):
                if v19[v22] == 0 or v18[v22] == 2:
                    v18[v22] -= 1
                    v20[v22] = True
                    v21.append(v22)
            while v21:
                v23 = collections.deque()
                for v22 in v21:
                    for v24 in v7[v22]:
                        v19[v24] -= 1
                        if v19[v24] == 0:
                            v18[v24] -= 1
                            if v20[v24]:
                                continue
                            v20[v24] = True
                            v23.append(v24)
                v21 = v23
            if all((x == 0 for v25 in v18)):
                if v17 < v12:
                    v12 = v17
                    v13 = [v15[:]]
                elif v17 == v12:
                    v13.append(v15[:])
        v26 = []
        v27 = ord('a')
        for v28 in v13:
            v29 = [0] * 26
            for v16 in range(v4):
                v29[ord(v1[v16]) - v27] = v28[v16]
            v26.append(v29)
        return v26
