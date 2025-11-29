import collections

class C1(object):

    def shortestPathLength(self, a1):
        """
        """
        v1 = [[float('inf')] * len(a1) for v2 in range(1 << len(a1))]
        v3 = collections.deque()
        for v4 in range(len(a1)):
            v1[1 << v4][v4] = 0
            v3.append((1 << v4, v4))
        while v3:
            v5, v6 = v3.popleft()
            v7 = v1[v5][v6]
            for v8 in a1[v6]:
                v9 = v5 | 1 << v8
                if v1[v9][v8] == float('inf'):
                    v1[v9][v8] = v7 + 1
                    v3.append((v9, v8))
        return min(v1[-1])
