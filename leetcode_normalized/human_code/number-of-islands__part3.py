import collections

class C1(object):

    def numIslands(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(a1, a2, a3):
            if a1[a2][a3] == '0':
                return False
            a1[a2][a3] = '0'
            v1 = collections.deque([(a2, a3)])
            while v1:
                v2, v3 = v1.popleft()
                for v4, v5 in v1:
                    v6, v7 = (v2 + v4, v3 + v5)
                    if not (0 <= v6 < len(a1) and 0 <= v7 < len(a1[0]) and (a1[v6][v7] == '1')):
                        continue
                    a1[v6][v7] = '0'
                    v1.append((v6, v7))
            return True
        v2 = 0
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                if bfs(a1, v3, v4):
                    v2 += 1
        return v2
