from collections import deque

class C1:

    def kEmptySlots(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * v1
        for v3, v4 in enumerate(a1):
            v2[v4 - 1] = v3
        v5 = a2
        v6 = [float('inf')] * (v1 - v5 + 1)
        v7 = deque()
        for v8 in range(v1):
            while v7 and v2[v7[-1]] >= v2[v8]:
                v7.pop()
            v7.append(v8)
            if v7[0] == v8 - v5:
                v7.popleft()
            if v8 >= v5 - 1:
                v6[v8 - v5 + 1] = v2[v7[0]]
        v9 = float('inf')
        for v10 in range(v1 - a2 - 1):
            v11 = v10 + a2 + 1
            v12 = max(v2[v10], v2[v11])
            v13 = v6[v10 + 1]
            if v13 > v12:
                v9 = min(v9, v12)
        return v9 + 1 if v9 < float('inf') else -1
