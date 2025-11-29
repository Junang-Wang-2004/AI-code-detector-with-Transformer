import collections

class C1(object):

    def shortestBridge(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def get_islands(a1):
            v1 = []
            v2 = set()
            for v3, v4 in enumerate(a1):
                for v5, v6 in enumerate(v4):
                    if v6 == 0 or (v3, v5) in v2:
                        continue
                    v7 = [(v3, v5)]
                    v8 = set(v7)
                    while v7:
                        v9 = v7.pop()
                        for v10 in v1:
                            v11 = (v9[0] + v10[0], v9[1] + v10[1])
                            if not (0 <= v11[0] < len(a1) and 0 <= v11[1] < len(a1[0])) or v11 in v8 or a1[v11[0]][v11[1]] == 0:
                                continue
                            v7.append(v11)
                            v8.add(v11)
                    v2 |= v8
                    v1.append(v8)
                    if len(v1) == 2:
                        break
            return v1
        v2, v3 = get_islands(a1)
        v4 = collections.deque([(node, 0) for v5 in v2])
        while v4:
            v5, v6 = v4.popleft()
            if v5 in v3:
                return v6 - 1
            for v7 in v1:
                v8 = (v5[0] + v7[0], v5[1] + v7[1])
                if not (0 <= v8[0] < len(a1) and 0 <= v8[1] < len(a1[0])) or v8 in v2:
                    continue
                v4.append((v8, v6 + 1))
                v2.add(v8)
