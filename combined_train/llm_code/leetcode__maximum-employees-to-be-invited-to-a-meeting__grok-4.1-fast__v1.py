from collections import deque

class C1:

    def maximumInvitations(self, a1):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1)]
        for v4 in range(v1):
            v2[a1[v4]].append(v4)
        v5 = [0] * v1
        v6 = []
        for v4 in range(v1):
            if v5[v4] != 0:
                continue
            v7 = {}
            v8 = 0
            v9 = v4
            while v5[v9] == 0:
                v5[v9] = 1
                v7[v9] = v8
                v8 += 1
                v9 = a1[v9]
            if v5[v9] == 1 and v9 in v7:
                v10 = v8 - v7[v9]
                v6.append((v9, v10))
            for v11 in v7:
                v5[v11] = 2

        def longest_chain(a1, a2):
            v1 = deque([a1])
            v2 = 0
            while v1:
                v2 += 1
                v3 = len(v1)
                for v4 in range(v3):
                    v5 = v1.popleft()
                    for v6 in v2[v5]:
                        if v6 == a2:
                            continue
                        v1.append(v6)
            return v2
        v12 = 0
        v13 = 0
        for v14, v10 in v6:
            if v10 > 2:
                v12 = max(v12, v10)
            elif v10 == 2:
                v15 = a1[v14]
                v13 += longest_chain(v14, v15) + longest_chain(v15, v14)
        return max(v12, v13)
