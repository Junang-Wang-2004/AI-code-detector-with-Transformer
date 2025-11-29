from collections import deque

class C1:

    def findLexSmallestString(self, a1, a2, a3):
        v1 = {a1}
        v2 = deque([a1])
        v3 = a1
        v4 = len(a1)
        while v2:
            v5 = v2.popleft()
            if v5 < v3:
                v3 = v5
            v6 = list(v5)
            for v7 in range(1, v4, 2):
                v8 = int(v6[v7])
                v6[v7] = str((v8 + a2) % 10)
            v9 = ''.join(v6)
            if v9 not in v1:
                v1.add(v9)
                v2.append(v9)
            v10 = v5[a3:] + v5[:a3]
            if v10 not in v1:
                v1.add(v10)
                v2.append(v10)
        return v3
