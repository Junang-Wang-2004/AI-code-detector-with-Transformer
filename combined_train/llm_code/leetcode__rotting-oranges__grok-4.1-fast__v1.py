import collections

class C1(object):

    def orangesRotting(self, a1):
        if not a1:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        v4 = 0
        v5 = collections.deque()
        for v6 in range(v1):
            for v7 in range(v2):
                if a1[v6][v7] == 2:
                    v5.append((v6, v7))
                elif a1[v6][v7] == 1:
                    v4 += 1
        v8 = 0
        while v5:
            v9 = len(v5)
            for v10 in range(v9):
                v11, v12 = v5.popleft()
                for v13, v14 in v3:
                    v15, v16 = (v11 + v13, v12 + v14)
                    if 0 <= v15 < v1 and 0 <= v16 < v2 and (a1[v15][v16] == 1):
                        a1[v15][v16] = 2
                        v4 -= 1
                        v5.append((v15, v16))
            if v5:
                v8 += 1
        return v8 if v4 == 0 else -1
