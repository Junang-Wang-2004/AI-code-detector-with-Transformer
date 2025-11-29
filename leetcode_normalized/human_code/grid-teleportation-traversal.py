import collections

class C1(object):

    def minMoves(self, a1):
        """
        """
        v1 = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        v2, v3 = (len(a1), len(a1[0]))
        v4 = [[] for v5 in range(26)]
        for v6 in range(v2):
            for v7 in range(v3):
                if a1[v6][v7] in '.#':
                    continue
                v4[ord(a1[v6][v7]) - ord('A')].append((v6, v7))
        v8 = [[False] * len(a1[0]) for v5 in range(v2)]
        v9 = collections.deque([(0, 0, 0)])
        while v9:
            v10, v6, v7 = v9.popleft()
            if v8[v6][v7]:
                continue
            v8[v6][v7] = True
            if (v6, v7) == (v2 - 1, v3 - 1):
                return v10
            for v11, v12 in v1:
                v13, v14 = (v6 + v11, v7 + v12)
                if not (0 <= v13 < v2 and 0 <= v14 < v3 and (a1[v13][v14] != '#') and (not v8[v13][v14])):
                    continue
                v9.append((v10 + 1, v13, v14))
            if a1[v6][v7] == '.':
                continue
            for v13, v14 in v4[ord(a1[v6][v7]) - ord('A')]:
                if v8[v13][v14]:
                    continue
                v9.appendleft((v10, v13, v14))
            v4[ord(a1[v6][v7]) - ord('A')] = []
        return -1
