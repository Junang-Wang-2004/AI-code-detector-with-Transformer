from collections import deque

class C1:

    def numberOfNodes(self, a1, a2):
        v1 = [0] * (a1 + 1)
        for v2 in a2:
            v1[v2] ^= 1
        v3 = 0
        v4 = deque([(1, 0)])
        while v4:
            v5, v6 = v4.popleft()
            v7 = v6 ^ v1[v5]
            v3 += v7
            v8 = 2 * v5
            v9 = v8 + 1
            if v8 <= a1:
                v4.append((v8, v7))
            if v9 <= a1:
                v4.append((v9, v7))
        return v3
