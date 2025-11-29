from collections import deque

class C1(object):

    def movesToStamp(self, a1, a2):
        v1 = len(a1)
        v2 = len(a2)
        if v1 == 0:
            return []
        v3 = v2 - v1 + 1
        v4 = [0] * v3
        v5 = [[] for v6 in range(v3)]
        v7 = [[] for v6 in range(v2)]
        for v8 in range(v3):
            for v9 in range(v1):
                v10 = v8 + v9
                if a2[v10] == a1[v9]:
                    v5[v8].append(v10)
                else:
                    v4[v8] += 1
                    v7[v10].append(v8)
        v11 = deque()
        v12 = [False] * v2
        v13 = []
        for v8 in range(v3):
            if v4[v8] == 0:
                v13.append(v8)
                for v10 in v5[v8]:
                    if not v12[v10]:
                        v12[v10] = True
                        v11.append(v10)
        while v11:
            v14 = v11.popleft()
            for v8 in v7[v14]:
                v4[v8] -= 1
                if v4[v8] == 0:
                    v13.append(v8)
                    for v10 in v5[v8]:
                        if not v12[v10]:
                            v12[v10] = True
                            v11.append(v10)
        return v13[::-1] if all(v12) else []
