from collections import deque

class C1(object):

    def wallsAndGates(self, a1):
        """
        """
        v1 = 2147483647
        v2 = deque([(i, j) for v3, v4 in enumerate(a1) for v5, v6 in enumerate(v4) if not v6])
        while v2:
            v3, v5 = v2.popleft()
            for v7, v8 in ((v3 + 1, v5), (v3 - 1, v5), (v3, v5 + 1), (v3, v5 - 1)):
                if 0 <= v7 < len(a1) and 0 <= v8 < len(a1[0]) and (a1[v7][v8] == v1):
                    a1[v7][v8] = a1[v3][v5] + 1
                    v2.append((v7, v8))
