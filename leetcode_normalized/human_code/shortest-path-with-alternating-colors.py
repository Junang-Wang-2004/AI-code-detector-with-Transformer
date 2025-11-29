import collections

class C1(object):

    def shortestAlternatingPaths(self, a1, a2, a3):
        """
        """
        v1 = [[set() for v2 in range(2)] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3][0].add(v4)
        for v3, v4 in a3:
            v1[v3][1].add(v4)
        v5 = max(2 * a1 - 3, 0) + 1
        v6 = [[v5, v5] for v3 in range(a1)]
        v6[0] = [0, 0]
        v7 = collections.deque([(0, 0), (0, 1)])
        while v7:
            v3, v8 = v7.popleft()
            for v4 in v1[v3][v8]:
                if v6[v4][v8] != v5:
                    continue
                v6[v4][v8] = v6[v3][1 ^ v8] + 1
                v7.append((v4, 1 ^ v8))
        return [x if x != v5 else -1 for v9 in map(min, v6)]
