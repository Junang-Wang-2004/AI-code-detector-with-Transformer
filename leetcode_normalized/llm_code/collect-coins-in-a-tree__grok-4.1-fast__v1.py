from collections import deque

class C1:

    def collectTheCoins(self, a1, a2):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a2:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = [len(v2[i]) for v7 in range(v1)]
        v8 = deque()
        for v7 in range(v1):
            if v6[v7] == 1 and (not a1[v7]):
                v8.append(v7)
        v9 = v1
        while v8:
            v10 = v8.popleft()
            if v6[v10] != 1 or a1[v10]:
                continue
            v11 = v2[v10][0]
            v2[v11].remove(v10)
            v2[v10] = []
            v6[v11] -= 1
            v6[v10] = 0
            v9 -= 1
            if v6[v11] == 1 and (not a1[v11]):
                v8.append(v11)
        v8 = deque((v7 for v7 in range(v1) if v6[v7] == 1))
        for v3 in range(2):
            v12 = deque()
            while v8:
                v10 = v8.popleft()
                if v6[v10] != 1:
                    continue
                v11 = v2[v10][0]
                v2[v11].remove(v10)
                v2[v10] = []
                v6[v11] -= 1
                v6[v10] = 0
                v9 -= 1
                if v6[v11] == 1:
                    v12.append(v11)
            v8 = v12
        return max(0, (v9 - 1) * 2)
