import collections

class C1(object):

    def maxDistance(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2 = collections.deque([(i, j) for v3 in range(len(a1)) for v4 in range(len(a1[0])) if a1[v3][v4] == 1])
        if len(v2) == len(a1) * len(a1[0]):
            return -1
        v5 = -1
        while v2:
            v6 = collections.deque()
            while v2:
                v7, v8 = v2.popleft()
                for v9, v10 in v1:
                    v11, v12 = (v7 + v9, v8 + v10)
                    if not (0 <= v11 < len(a1) and 0 <= v12 < len(a1[0]) and (a1[v11][v12] == 0)):
                        continue
                    v6.append((v11, v12))
                    a1[v11][v12] = 1
            v2 = v6
            v5 += 1
        return v5
