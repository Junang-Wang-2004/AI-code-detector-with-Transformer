import collections

class C1(object):

    def orangesRotting(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2 = 0
        v3 = collections.deque()
        for v4, v5 in enumerate(a1):
            for v6, v7 in enumerate(v5):
                if v7 == 2:
                    v3.append((v4, v6, 0))
                elif v7 == 1:
                    v2 += 1
        v8 = 0
        while v3:
            v4, v6, v8 = v3.popleft()
            for v9 in v1:
                v10, v11 = (v4 + v9[0], v6 + v9[1])
                if not (0 <= v10 < len(a1) and 0 <= v11 < len(a1[v4])):
                    continue
                if a1[v10][v11] == 1:
                    v2 -= 1
                    a1[v10][v11] = 2
                    v3.append((v10, v11, v8 + 1))
        return v8 if v2 == 0 else -1
