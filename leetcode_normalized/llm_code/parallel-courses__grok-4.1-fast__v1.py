from collections import deque, defaultdict

class C1:

    def minimumSemesters(self, a1, a2):
        v1 = defaultdict(list)
        v2 = [0] * a1
        for v3, v4 in a2:
            v1[v3 - 1].append(v4 - 1)
            v2[v4 - 1] += 1
        v5 = deque((i for v6 in range(a1) if v2[v6] == 0))
        v7 = 0
        v8 = a1
        while v5:
            v7 += 1
            v9 = len(v5)
            for v10 in range(v9):
                v11 = v5.popleft()
                v8 -= 1
                for v12 in v1[v11]:
                    v2[v12] -= 1
                    if v2[v12] == 0:
                        v5.append(v12)
        return v7 if v8 == 0 else -1
